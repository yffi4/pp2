import psycopg2, re

conn = psycopg2.connect(
    host='localhost',
    database='phonebook1',
    user='postgres',
    password='15103016',
    port=5432
)

cur = conn.cursor()

cur.execute(
    '''CREATE OR REPLACE FUNCTION search_from_book(a VARCHAR)
      RETURNS SETOF phonebook1_list
   AS
   $$
      SELECT * FROM phonebook1_list WHERE full_name = a;
   $$
   language sql;
   '''
)

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_list_of_users(
   IN users TEXT[][]
 )

 LANGUAGE plpgsql

 AS $$

 DECLARE
   i TEXT[];

 BEGIN 

    Foreach i slice 1 in array users
    LOOP
       INSERT INTO phonebook1_list (full_name, phone_number) VALUES (i[1], i[2]);
    END LOOP;

 END
 $$;
 '''
)

cur.execute(
    '''CREATE OR REPLACE PROCEDURE insert_to_book(nm VARCHAR, phon VARCHAR)
       LANGUAGE plpgsql
       AS $$
       DECLARE 
          cnt INTEGER;
       BEGIN
          SELECT INTO cnt (SELECT count(*) FROM phonebook1_list WHERE full_name = nm);
          IF cnt > 0 THEN
             UPDATE phonebook1_list
                SET phone_number = phon
                WHERE full_name = nm;
          ELSE
             INSERT INTO phonebook1_list(full_name, phone_number) VALUES (nm, phon);
             END IF;
       END;
       $$;''')

cur.execute("""CREATE OR REPLACE PROCEDURE delete_from_book(nm VARCHAR)
LANGUAGE plpgsql
AS $$
DECLARE cnt INTEGER;
BEGIN
    SELECT into cnt (SELECT count(*) FROM phonebook1_list WHERE full_name = nm);
  IF cnt IS NOT NULL THEN
        DELETE FROM phonebook1_list
    WHERE name=nm;
    END IF;
END;
$$;""")

cur.execute("""CREATE OR REPLACE FUNCTION paginatingfrom(a integer, b integer)
RETURNS SETOF phonebook1_list
AS $$
   SELECT * FROM phonebook1_list
  ORDER BY full_name
  LIMIT a OFFSET b;
$$
language sql;""")

a = input()
if a == 'search':
    print("Введите имя:")
    name = input()
    cur.execute(f"SELECT search_from_book((\'{name}\'))")
    result = cur.fetchall()
    print(result[0])
if a == 'insert':
    print("Введите имя:")
    name = input()
    print("Введите номер телефона:")
    phone = input()
    cur.execute(f"CALL insert_to_book((\'{name}\'),(\'{phone}\'))")
if a == 'insertloop':
    cur.execute('''CALL insert_list_of_users(ARRAY[
    ARRAY['Danabek', '87076052769'],
    ARRAY['Kayirzhan', '87079815569'],
    ARRAY['Bexultan', '87074793780']
]);''')
if a == 'delete':
    name = input()
    cur.execute(f"CALL delete_from_book (\'{name}\')")
if a == 'paginating':
    cur.execute(
        '''SELECT * FROM paginatingfrom(6, 0);'''
    )
    print(cur.fetchall())
conn.commit()
cur.close()
conn.close()
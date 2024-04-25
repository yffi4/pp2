import psycopg2
import csv
conn = psycopg2.connect(database = "phonebook1",
                        user = "postgres",
                        host = "localhost",
                        password = "15103016",
                        port = 5432)


cur = conn.cursor()

def insert_data_from_csv(): #добавление новых данных с помощью csv файла
    with open('pb_data.csv', 'r', encoding='UTF-8') as f:
        cur.copy_from(f, 'phonebook1_list', sep=',')
        conn.commit()

def insert_data_from_console(): #добавление новых данных с помощью консоли
    number_id = input("Enter id: ")
    full_name = input("Enter full name: ")
    phone_number = input("Enter phone number: ")
    cur.execute(
        "INSERT INTO phonebook1_list (number_id, full_name, phone_number) VALUES (%s, %s, %s)",
        (number_id, full_name, phone_number)
    )
    conn.commit()

def updating_data():
    cur.execute("UPDATE phonebook1_list SET phone_number = '+7 705 133 1223' WHERE number_id = '3';")
    conn.commit()

def select_from_data():
    print(cur.execute("SELECT FROM phonebook1_list phone_number WHERE number_id ='3';"))

def delete_from_data():
    cur.execute("DELETE FROM phonebook1_list WHERE number_id = '1';")
    conn.commit()

delete_from_data()
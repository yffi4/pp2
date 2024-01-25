def peverse(str):
    lst = []
    for i in str:
        lst.append(i)
    print(lst[::-1])


peverse(input().split())

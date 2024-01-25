def uniq_elements(n):
    lst = []
    for i in n:
        if i not in lst:
            lst.append(i)

    return lst


lst = [1, 2, 2, 3, 3, 3, 10, 24, 11, 11]
print(uniq_elements(lst))
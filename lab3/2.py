def convert_faringate_to_celcia(faringate):
    celcia = (5 / 9) * (faringate - 32)
    return faringate


faringate = float(input())
print(convert_faringate_to_celcia(faringate))

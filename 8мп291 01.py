y = int(input("Введіть номер року: "))

if y % 100 == 0:
    C = y // 100
else:
    C = y // 100 + 1

print("Номер століття: ", C)

print("Введіть ціле число:")
input_value = input()
while not input_value.isdigit():
    print("Введене значення не є цілим числом. Спробуйте ще раз.")
    input_value = input()
a = int(input_value)
print("Ви ввели число а =", a)

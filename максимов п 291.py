while True:
    try:
        input_value = int(input("Введіть ціле число: "))
        break
    except ValueError:
        print("Введене значення не є цілим числом. Спробуйте ще раз.")

a = input_value

print("Ви ввели число а =", a)

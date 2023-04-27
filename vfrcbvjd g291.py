while True:
    try:
        input_value = float(input("Введіть дійсне число: "))
        break
    except ValueError:
        print("Введене значення не є дійсним числом. Спробуйте ще раз.")

a = input_value

print("Ви ввели число а =", a)

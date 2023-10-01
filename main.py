numeric = input("Введіть ціле числове значення : ")

if not numeric.isdigit():
    print("Введене значення повинне бути цілим числом")
    numeric = input("Введіть значення ще раз : ")

for symbol in numeric:
    int_number = int(symbol)
    row = "#" * int_number
    print(symbol + " - " + row)

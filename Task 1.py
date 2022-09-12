# Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = float(input("Введите число: "))

lst = list(str(number).split('.'))
summ = 0
for i in lst:
    for j in i:
        summ += int(j)

new_sum = sum(map(int, str(number).replace('.', '')))
print(f"Сумма цифр числа равна = {new_sum}")
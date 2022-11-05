"""
Напишите программу, которая считывает с клавиатуры два числа a и b, считает
и выводит на консоль среднее арифметическое всех чисел из отрезка
[a; b], которые кратны числу 3.
"""
a, b = (int(input()) for i in range(2))
summa = 0
count = 0
while a % 3 != 0:
    a += 1
# print(a, b) # проверка
for i in range(a, b + 1, 3):
    summa += i
    count += 1
print(summa / count)

# альтернативное  решение
# a,b = int(input()), int(input())
# a += -a%3
# b -= b%3
# print((a+b)/2)


# a = int(input())
# b = int(input())
# while a % 3 != 0:
#     a += 1
# while b % 3 != 0:
#     b -= 1
# print((a+b)/2)

# a, b = (int(input()) for _ in range(2))
# print((a + (3 - a % 3) + b - (b % 3)) / 2)

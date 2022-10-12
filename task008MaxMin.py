"""
Напишите программу, которая получает на вход три целых числа, по одному числу в строке,
и выводит на консоль в три строки сначала максимальное, потом минимальное,
после чего оставшееся число.
На ввод могут подаваться и повторяющиеся числа.
"""

# array = [int(input()), int(input()), int(input())]
# print(max(array), min(array), sep="\n")
# array.remove(max(array))
# array.remove(min(array))
# print(array[0])

# array = [int(input()) for i in range(3)]
# print(max(array), min(array), sum(array) - max(array) - min(array), sep="\n")
#
# x = sorted([int(input()), int(input()), int(input())])
# print(x[2], x[0], x[1], sep="\n")

a, b, c = int(input()), int(input()), int(input())
if a < b: a, b = b, a
if a < c: a, c = c, a
if b < c: c, b = b, c
print(a, c, b, sep='\n')

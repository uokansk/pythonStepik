"""
Напишите программу, которая принимает на вход список чисел в одной строке и
выводит на экран в одну строку значения, которые встречаются в нём более одного раза.
Для решения задачи может пригодиться метод sort списка.
Выводимые числа не должны повторяться, порядок их вывода может быть произвольным.
"""
a = [int(i) for i in input().split()]
a.sort()
new_List = []
i = 0
cnt = 1
for i in range(0, len(a), cnt):
    # print(cnt)
    if a.count(a[i]) > 1:
        new_List = a[i]
        cnt = a.count(a[i])
        print(i, '\t', cnt, '\t', new_List)
    # cnt = a.count(a[i])

# def more_than_two(numbers):
#     n2 = [n for n in numbers if numbers.count(n) > 1]
#     S = set(n2)
#     print(' '.join(str(s) for s in S))
#
# s = [int(i) for i in input().split()]
# more_than_two(s)


# a = [int(i) for i in input().split()]
# a.sort()
# new_List = []
# for i in range(len(a) - 1):
#     if (a[i] == a[i + 1] and i + 1 == len(a)-1) or (a[i] == a[i + 1] and a[i] != a[i + 2]):
#         new_List = a[i]
#         print(new_List, end=' ')


# a, b = [int(i) for i in input().split()], []
# for i in a:
#     if a.count(i) > 1 and b.count(i) == 0:
#         b.append(i)
#         print(i, end=' ')
# # for i in b:
# #     print(i, end=' ')

"""
Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.
Используйте метод split строки.
"""

# a = [int(i) for i in input().split()]
# summaList = 0
# for i in a:
#     summaList += i
# print(summaList)


"""
Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого списка вывести сумму двух его соседей.
Для элементов списка, являющихся крайними, одним из соседей считается элемент,
находящий на противоположном конце этого списка. Например, если на вход подаётся
список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).
"""

a = [int(i) for i in input().split()]
sList = []
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        sList = a[i - 1] + a[i - (len(a)-1)]
        print(sList, end=' ')



# text = [int(i) for i in input().split()]
# long = len(text)
# sum_list = []
#
# left_index = -1
# right_index = -len(text) + 1
# middle_index = 0
#
# if long == 1:
#     sum_list = text
# else:
#     while middle_index < long:
#         sum_list.append(text[left_index] + text[right_index])
#         left_index += 1
#         right_index += 1
#         middle_index += 1
# print(*sum_list)


# a = [int(i) for i in input().split()]
# a.sort()
# new_List = []
# for i in range(len(a) - 1):
#     if (a[i] == a[i + 1] and i + 1 == len(a)-1) or (a[i] == a[i + 1] and a[i] != a[i + 2]):
#         new_List = a[i]
#         print(new_List, end=' ')

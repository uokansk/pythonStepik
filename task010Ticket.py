# number = int(input())
# a = number // 100000
# b = number // 10000 % 10
# c = number // 1000 % 10
# d = number // 100 % 10
# e = number // 10 % 10
# f = number % 10
# if a + b + c == d + e + f:
#     print("Счастливый")
# else:
#     print("Обычный")


# a = input()
# if int(a[0]) + int(a[1]) + int(a[2]) == int(a[3]) + int(a[4]) + int(a[5]):
#     print('Счастливый')
# else:
#     print('Обычный')
# print(a[0], a[1], a[2], a[3], a[4], a[5], sep="\n")

i = 0
while i < 5:
    print('*')
    if i % 2 == 0:
        print('**')
    if i > 2:
        print('***')
    i = i + 1

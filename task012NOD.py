# number = 0
# while number < 100:
#     number = int(input())
#     if number < 10:
#         continue
#     elif number > 100:
#         break
# print(number)

# i = 0
# while int(i) <= 100:
#     i = int(input())
#     if 10 <= int(i) <= 100:
#         print(i)
#     else:
#         continue

# number = 0
# while number <= 100:
#     number = int(input())
#     if 10 <= number <= 100:
#         print(number)

# a, b, c, d = (int(input()) for i in range(4))
# for i in range(a, b + 1):
#
#     for j in range(c, d + 1):
#         print(j, end='\t')
#     print(i, sep='\n')


# a = [int(input()) for i in range(10)]
# print(sum(a))
#
# s = 0
# for i in range(10):
#     s = s + int(input())
# print(s)

# s = 0
# a = int(input())
# for i in range(a):
#     s = s + int(input())
# print(s)

# s = 0
# a = int(input())
# for i in range(1, a + 1):
#     s += i ** 3
# print(s)

# a, b, c, d = (int(input()) for i in range(4))
# for j in range(c, d + 1):
#     print('\t', j, end='')
# print()
# for i in range(a, b + 1):
#     print(i, end=' ')
#     for j in range(c, d + 1):
#         print('\t', i * j, end="")
#     print()

# a = int(input())
# for i in range(1, a+1):
#     print()
#     for j in range(1, i+1):
#         print(j, end='')


# n = int(input())
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end = '')
#     print()

# num_zeroes = 0
# for i in range(int(input())):
#     if int(input()) == 0:
#         num_zeroes += 1
# print(num_zeroes)
a, b, l, N = (int(input()) for i in range(4))
laceLength = (N-1)*b*2 + l*2 + (N-1)*a*2 +a
print(laceLength)

# currentCard = 0
# if currentCard
# for i in range(1, countCard):
#     currentCard = int(input())
#     print(i)
#     for j in range(1, countCard):
#         print(currentCard)
#     # if i != currentCard:
#     #     print(i)
#     #     # break

# Тимофей обычно спит ночью XX часов и устраивает себе днем
# тихий час на YY минут.
# Определите, сколько всего минут Тимофей спит в сутки.

# hour = int(input())
# minute = int(input())
# print(hour * 60 + minute)

x, y = (int(input()) for i in range(2))
print(x * 60 + y)

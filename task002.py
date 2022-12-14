# Тимофей обычно спит ночью XX часов и устраивает себе днем
# тихий час на YY минут.
# Определите, сколько всего минут Тимофей спит в сутки.

# hour = int(input())
# minute = int(input())
# print(hour * 60 + minute)

# x, y = (int(input()) for i in range(2))
# print(x * 60 + y)

##################################
# Коля каждый день ложится спать ровно в полночь и недавно узнал,
# что оптимальное время для его сна составляет XX минут.
# Коля хочет поставить себе будильник так, чтобы он прозвенел
# ровно через XX минут после полуночи, однако для этого необходимо
# указать время сигнала в формате часы, минуты. Помогите Коле
# определить, на какое время завести будильник.
###################################

# sleepTime = int(input())
# print(sleepTime // 60)
# print(sleepTime % 60)

# print(*divmod(int(input()), 60), sep='\n')

# X = int(input())
# print(f"{X // 60}\n{X % 60}")


##################################
# Катя узнала, что ей для сна надо X минут. В отличие от Коли, Катя ложится
# спать после полуночи в HH часов и MM минут. Помогите Кате определить, на
# какое время ей поставить будильник, чтобы он прозвенел ровно через X минут
# после того, как она ляжет спать.
######################################

# x = int(input())
# H = int(input())
# M = int(input())
# H = H * 60 + M + x
# a = H // 60
# b = H % 60
# print(a)
# print(b)

sleepTime, hour, minute = (int(input()) for i in range(3))
alarmTime = hour * 60 + minute + sleepTime
print(f"{alarmTime // 60}\n{alarmTime % 60}")

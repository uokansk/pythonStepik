# Из передачи “Здоровье” Аня узнала, что рекомендуется спать хотя бы A часов в сутки,
# но пересыпать тоже вредно и не стоит спать более B часов. Сейчас Аня спит H часов
# в сутки. Если режим сна Ани удовлетворяет рекомендациям передачи “Здоровье”, выведите
# “Это нормально”. Если Аня спит менее A часов, выведите “Недосып”, если же более B
# часов, то выведите “Пересып”.
# Получаемое число A всегда меньше либо равно B.
# На вход программе в три строки подаются переменные в следующем порядке: A, B, H.
# Обратите внимание на регистр символов: вывод должен в точности соответствовать
# описанному в задании, т. е. если программа должна вывести "Пересып", выводы программы
# "пересып", "ПЕРЕСЫП", "ПеРеСыП" и другие не будут считаться верными.


# a, b, h = (int(input()) for _ in range(3))
normSleep, bigSleep, factSleep = int(input()), int(input()), int(input())
if factSleep < normSleep:
    print('Недосып')
elif factSleep > bigSleep:
    print('Пересып')
else:
    print('Это нормально')
# print(normSleep)
# print(bigSleep)
# print(factSleep)

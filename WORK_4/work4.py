# Задача 4: Требуется определить, можно ли от шоколадки
# размером n × m долек отломить k долек, если разрешается
# сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('ВВЕДИТЕ ДЛИНУ: '))
m = int(input('ВВЕДИТЕ ШИРИНУ: '))
k = int(input('ВВЕДИТЕ КОЛИЧЕСТВО ДОЛЕК: '))

# sh = n * m
# s = sh - k
# m = k // n
# if :m == sh
#    print('YES')
# else:
#    print('NO')

if k < m * n and k % m == 0 :
    print('YES')
else:
    print('NO')

#Задача1: Напишите программу, которая принимает на вход вещественное число
#  и показывает сумму его цифр.


# count = 0
# a = str(input())
# for i in range(0, len(a)):
#     if a[i].isdigit():
#         b = int(a[i])
#         count += b
# print(count)


#Задача2: Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.

# n = int(input())
# a = []

# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     a.append(factorial)
# print(a)

# Задача3: Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input())
# a = []

# for i in range(1,n+1):
#     pr = (1 + (1/i))**i
#     a.append(pr)
# print(a)


#Задача 4: Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

inFile = open('file.txt', 'r', encoding='utf8')

a = []
for line in inFile:
    a.append(int(line))
N = a[0]
a.remove(N)

b = []
for i in range(-N, N+1):
    b.append(i)

count = 1
for i in a:
    count *= b[i]
print(count)

inFile.close()

# Задача 5: Реализуйте алгоритм перемешивания списка.

# a = list(range(1, 100, 10))
# print(a)
# import random
# random.shuffle(a)
# print(a)

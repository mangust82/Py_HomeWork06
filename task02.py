# 2 Напишите программу, которая принимает на вход число N и выдает набор произведений 
# чисел от 1 до N.
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math

num = int(input('Enter the number '))
list2 = [math.factorial(x) for x in range(1, num+1)]
print(list2)

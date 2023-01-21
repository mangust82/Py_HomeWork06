# Напишите программу, которая принимает на вход вещественное число и показывает сумму 
# его цифр.
from functools import reduce

num = input('Enter the real number ')
glue_list = ''.join(num.split('.'))
sum = reduce((lambda x, y: int(x)+int(y)), glue_list)
print(sum)

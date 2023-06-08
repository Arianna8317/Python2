"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.
"""
from fractions import Fraction

def reduce_fractal(a, b):
    if a > b:
        limit = b
    else:
        limit = a
    for i in range(2, limit):
        while (not a % i) and (not b % i):
            a = a / i
            b = b / i
    return int(a), int(b)


def fractal_calculator(fr1, fr2):
    fr_a = fr1.split("/")
    fr_b = fr2.split("/")
    num_a = int(fr_a[0])
    denom_a = int(fr_a[1])   
    num_b = int(fr_b[0])
    denom_b = int(fr_b[1]) 
    sum = reduce_fractal(num_a*denom_b+num_b*denom_a, denom_a*denom_b)
    product = reduce_fractal(num_a*num_b, denom_a*denom_b)  
    return str(sum[0])+'/'+str(sum[1]), str(product[0]) + '/' + str(product[1])


print(fractal_calculator("3/25", "8/120"))
print(Fraction(3, 25)+Fraction(8, 120), Fraction(3, 25)*Fraction(8, 120))
print(fractal_calculator("2/13", "3/26"))
print(Fraction(2, 13)+Fraction(3, 26), Fraction(2, 13)*Fraction(3, 26))
#print(reduce_fractal(75, 625))
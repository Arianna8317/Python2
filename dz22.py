# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def dec_hex(number):
    my_binary = ""
    while number > 0:
        remainder = number % 16
        if remainder > 9:
            if remainder == 10:
                str_remainder = 'A'
            elif remainder == 11:
                str_remainder = 'B' 
            elif remainder == 12:
                str_remainder = 'C' 
            elif remainder == 13:
                str_remainder = "D"
            elif remainder == 14:
                str_remainder = "E"  
            elif remainder == 15:
                str_remainder = "F"   
        else:
            str_remainder = str(remainder)               
        my_binary = str_remainder + my_binary
        number = number // 16
    return my_binary   
 

while True:
    str_num = input('Введите натуральное число < 100000 : ')   
    if str_num.isdigit():
        num = int(str_num)   
        if num > 1 and num < 100000:
            break

print(dec_hex(num)) 
# или встроенная функция
print(hex(num))
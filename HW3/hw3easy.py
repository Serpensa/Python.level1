# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    pass


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


def my_round(number, ndigits):
    n1 = number * (10 ** ndigits)
    dot = len(str(int(n1))) + 1
    if int(str(n1)[dot]) > 5:
        n1 += 1
    return float(int(n1) / (10 ** ndigits))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    pass

def lucky_ticket(ticket_number):
    tnumber_str=str(ticket_number)
    tnumber_list= list(map(int, tnumber_str))
    if len(tnumber_str)!= 6:
        return "Неверный номер"
    else:
            sum1 = sum(tnumber_list[:3])
            sum2 = sum(tnumber_list[3:])
            if sum1==sum2:
                return "Счастливый билет"
            else:
                return "Oбычный билет"

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
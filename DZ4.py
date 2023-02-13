task = int(input('введите номер залачи от 1 до 2:'))
match task:
    case 1:
# Задача 1
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
      
       
        def stepen(a, n):
            global result
            if n > 0:
                result = result * a
                n -= 1
                stepen(a, n)
            else:
                print(result)

        
           
        numbre_A = int(input('Введите число которое будем возводить в степень:  '))
        numbre_B = int(input('Введите степень, которую будем возводить :  '))
        result =1
        stepen(numbre_A,numbre_B)

    case 2:
# Задача 2
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4
      
       def summa(a, b):
        result =1

        if b != 0:
            a +=1
            b -=1
            summa(a,b)
        else: print(a)
           
       numbre_A = int(input('Введите число A:  '))
       numbre_B = int(input('Введите Число B:  '))
       
       summa(numbre_A,numbre_B)
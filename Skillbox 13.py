#!/usr/bin/env python
# coding: utf-8

# In[63]:


#Задание 1 

def summa_n(n):
    count = 0
    y = 1
    for x in range(n+1): 
        count += x
    print("Я знаю, что сумма чисел от 1 до",n,"равна",count)
    
n = int(input("Введите число n: "))    
summa_n(n)


# In[2]:


#Задание 2
def test():
    question = int(input("Введите число: "))
    if question > 0: 
        positive()
    elif question < 0: 
        negative()
        
def positive(): 
    print("Положительное")
    
def negative(): 
    print("Отрицательное")
    
test()


# In[97]:


#Задание 3
def calculator(question,number):
    question = int(input(" 1 вывести сумму числа, 2 вывести максимальную цифру, 3 вывести минимальную цифру, 0 остановить программу"))
    number = int(input("Введите число: ")) 
    if question == 1: 
        summa(number)
    elif question == 2: 
        max_number(number)
    elif question == 3: 
        min_number(number)
    elif question == 0: 
        print("программа остановленна")
    else: 
        print("Обшибка ввода")
        calculator(question,number)
        
def summa(number): 
    answer = sum(map(int,str(number)))
    print("Сумма чисел = ",answer)
    calculator(question,number)

def max_number(number): 
    m = max([int(i) for i in str(number)])
    print("Наибольшая цифра: ",m)
    calculator(question,number)
    
def min_number(number):
    n = min([int(i) for i in str(number)])
    print("Наименьшая цифра: ",n)
    calculator(question,number)


calculator(question,number)


# In[41]:


#Задание 4
n = 1 
while n != 0: 
    d,dd = 10,1
    s = " "
    n = int(input("Введите число которое переворачиваем:  "))
    if n == 0: 
        print("Программа завершена ")
        break
    for i in range(len(str(n))):
        s+= str(n%d//dd)
        d*= 10
        dd*=10
    print("Перевернутое число: ", s)
    print("Отчищенное от нолей: ",(int(str(s).replace('0',''))))
    
    


# In[12]:


#Задание 5
def score():
    k0=n0=0
    for i in t:
        if i==k: k0+=1
        if i==n: n0+=1
    print(f"Количество цифр {k}: {k0}\nКоличество букв {n}: {n0}")

t = input('Введите текст: ')
k = input('Какую цифру ищем? ')
n = input('Какую букву ищем? ')
score()


# In[21]:


#Задание 8
a = int(input())
b = int(input())
 
# Пока какое-нибудь из двух числе не будет равно 0,
while a != 0 and b != 0:
    # сравнивать их между собой.
    # Если первое число больше второго,
    if a > b:
        # то находить остаток от деления его на второе число 
        # и присваивать его первой переменной
        a = a % b
    # Иначе (когда второе число больше первого)
    else:
        # присваивать второй переменной остаток от деления 
        # нацело второго числа на первое
        b = b % a
 
# Одно из чисел содержит 0, а другое - НОД, но какое - неизвестно.
# Проще их сложить, чем писать конструкцию if-else
gcd = a + b
print("НОД: ",gcd)


# In[59]:


#Задание 7
def minimum(x):
    print(min(x))
    x=list(map(int,input().split()))
    minimum(x)


# In[86]:


#Задание 6 (Сомневаюсь что верно решено)
def f(x,y,step): 
    if (-step<=x<=step) and (-step<=y<=step): 
        print('Где-то рядом')
    else: 
        print('Монетки в области нет')

        
x = int(input())  
y = int(input())  
step = 1
f(x,y,step)


# In[4]:


#### Задание 9
import random
import math

def rock_paper_scissors():
    ver = 0
    while (ver == 0):
        player = int(input("1 - камень, 2 - ножницы, 3 - бумага. "))
        if (player == 1 or player == 2 or player == 3):
            ver = 1    
    if player == 1:
        print("Вы выбрали камень.")  
    if player == 2:
        print("Вы выбрали ножницы.") 
    if player == 3:
        print("Вы выбрали бумагу.")  
    comp = random.randint(1, 3)
    if comp == 1:
        print("Компьютер выбрал камень.") 
    if comp == 2:
        print("Компьютер выбрал ножницы.")
    if comp == 3:
        print("Компьютер выбрал бумагу.")
    # определяем победителя
    if player == comp:
        win = 0
    if player == 1 and comp == 2:
        win = 1 
    if player == 1 and comp == 3:
        win = 2 
    if player == 2 and comp == 1:
        win = 2  
    if player == 2 and comp == 3:
        win = 1 
    if player == 3 and comp == 1:
        win = 1
    if player == 3 and comp == 2:
        win = 2
    if win == 0:
        print("Ничья!")
    if win == 1:
        print("Победил игрок!")
    if win == 2:
        print("Победил компьютер!")
        
def guess_the_number():

    from random import randint
 
    attempts = 1
    Var1 = randint(1,100)
    print ("Загадано число от 1 до 99")
    Var2 = int(input("Ваш вариант? - "))
    while Var1 != Var2:
        if Var1 > Var2: print (f"Угадываемое число больше {Var2} ")
        elif Var1 < Var2: print (f"Угадываемое число меньше {Var2} ")
        attempts += 1
        Var2 = int(input("Ваш вариант? - "))
    print (f"Вы угадали число {Var1} за {attempts} попыток ")

def mainMenu():
    question = int(input("Выберите игру: 1 - камень, ножницы, бумага. 2 - Угадай число. 0 - завершить.  "))
    if question == 1: 
        print("Вы выбрали камень, ножницы, бумага")
        rock_paper_scissors()
        mainMenu()
    elif question == 2: 
        print("Вы выбрали угадай число")
        guess_the_number() 
        mainMenu()
    elif question == 0: 
        print("Игры завершены, досвидание")
    else: 
        print("Ошибка ввода")
        
        
mainMenu()


# In[5]:


#Задание 10
level={
    0:('Вы в незнакомой квартире. И вам нужно выбраться',{'осмотреться':1}, {"стоп":9}),
    1:('Вы в спальне. Куда пойти?',{'в ванную':2,'в коридор':4}),
    2:('Вы в ванной. Куда пойти?',{'в спальню':1,'в коридор':4}),
    3:('Вы на кухне. Здесь есть окно. Куда пойти?',{'в окно':5,'в коридор':4}),
    4:('Вы в коридоре. Куда пойти?',{'в ванную':2,'в спальню':1,'на кухню':3,'в дверь':6}),
    5:('Вы разбиваете окно, выпрыгиваете в него и падаете. Причем долго - этаж был далеко не первый. Вы проиграли.',{'заново?':0}),
    6:('Вы открываете дверь. Удивительно, она не заперта! Вы выиграли.',{'заново?':0})
    }
def change(lvl,):
    a,b,c=level[lvl],{},1
    print(a[0])
    for i in a[1]:
        print('%s - %s'%(c,i))
        b[str(c)],c=a[1][i],c+1
    while 1:
        d=input()
        if d in b:
            break
        elif d =='0':
            exit()
        else:
            print('Неправильно набран номер!')
    change(b[d])
change(0)


# In[10]:


def summa_n (n): 
    y = 0
    for x in range (1,n+1,1): 
        y += x 
    print("Сумма от 1 до",n,"=",y)
    return y 
    
        
question = int(input("Введите число: "))
new_n = summa_n (question)
summa_n (new_n)


# In[8]:


def gcd(a,b): 
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    gcd = a + b
    print("НОД: ",gcd)
    return a,b

a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
gcd(a,b)


# In[32]:


summa_n = int(input("Введите колличество задач: "))
for x in range(summa_n): 
    count = int(input("Введите число: "))
numeral_count(summa_n)
    
def numeral_count(number):
    if number < 0: 
        print("число отрицательное! Обнуляю.")
        return 0 
    new_count = 0
    while number > 0: 
        number //= 10
        new_count += 1
    return(new_count)



#Numeral = numeral_count(summa_n)


# In[36]:


def numeral_count(n):
    result = 0
    while n > 0:
        result += 1
        n //= 10
    return result
    
print("Пример работы программы:")
n = int(input("Введите кол-во задач: "))
print(f"\nПервая задача на обработку: {max((int(input('Введите число: ')) for _ in range(n)), key=numeral_count)}")


# In[ ]:





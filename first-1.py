import math
x=input("Введите строку:\n ")
#1.1
if x.isnumeric():
    print("Строка из цифр")
else:
    print("В строке не только цифры")
#1.2
space=0
for i in range(len(x)-1):
    if x[i]==" ":
        space+=1
print("Количество проблелов: " + str(space))

#1.3
point=0
for i in range(len(x)-1):
    if x[i]==".":
        point+=1
print("Количество точек: " + str(point))

#1.4
x="Homework"
full_string=46*" "+x+46*" "
print(full_string)

#1.4.1
x="Homework"
new_str=x.center(100)
print(new_str)

#1.5
x=input("введите строку для 5 задания: \n")
y = x[0].upper()
for i in range(0,len(x)-1):
    if x[i]==" ":
        y=y+(x[i+1].upper())
    else:
        y=y+x[i+1]
print("Новая строка: " +y)


#2.1
a=179
b=971
c=math.sqrt(a**2+b**2)
print(c)

#2.2
x=int(input("введите двухзначное число: \n"))
y=x//10
print("число десятков: "+str(y))

#2.3
x=int(input("введите трехзначное число: \n"))
y=x//100
z=(x-100*y)//10
w=(x-y*100-z*10)
x_new=y+z+w
print("сумма цифр: "+str(x_new))

#2.4
n=int(input("введите целое число: \n"))
if n%2==0:
    print("следующее четное чилос "+str(n+2))
else:
    print("следующее четное чилос " + str(n + 1))

#2.5
n=float(input("введите положительное вещественное число: \n"))
print(math.modf(n)[0])


#2.6
n=float(input("введите положительное вещественное число: \n"))
k=10*math.modf(n)[0]
print(int(math.modf(k)[1]))


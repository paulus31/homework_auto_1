#7.1
print("Задача 7.1")
x=0
while x<11:
    print(x)
    x+=1

#7.2
print("Задача 7.2")
x=20
while x>0:
    print(x)
    x-=1

#8.1
print("Задача 8.1")
x=[]
k=''
while k!="Exit":
    k=input("Введите число для добавления в массив: , для завершения ввода наберите Exit \n")
    if k=="Exit":
        pass
    else:
        x.append(k)
else:
    pass
l=len(x)-1
print(l)
i=0
while i<=l:
    x.pop(0)
    i+=1
    print(x)

#8.2
print("Задача 8.2")
x=[]
k=''
while k!="Exit":
    k=input("Введите число для добавления в массив: , для завершения ввода наберите Exit \n")
    if k=="Exit":
        pass
    else:
        x.append(int(k))
else:
    pass
l=len(x)-1
x.sort()
print(x)
i=0
while i<=l:
    x.pop(0)
    i+=1
    print(x)


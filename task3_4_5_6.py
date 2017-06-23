#1.3
x=int(input("Введите год: "))
if x%4==0:
    if x%100!=0:
        print("год високосный")
    elif x%100==0 and x%400==0:
        print("год високосный")


#1.4
a=float(input("Введите 1 сторону треугольника: "))
b=float(input("Введите 2 сторону треугольника: "))
c=float(input("Введите 3 сторону треугольника: "))
if a+b>c and a+c>b and b+c>a:
    print("YES")
else:
    print("NO")

#1.5
a = float(input("Введите 1 число: "))
b = float(input("Введите 2 число: "))
if a>b:
    a,b=b,a
c = float(input("Введите 3 число: "))
if b>c:
    b,c=c,b

print(a, b, c)


#1.6
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
c = int(input("Введите 3 число: "))
if a==b:
    if b==c:
        print("3")
    else:
        print("2")
else:
    if b==c:
        print("2")
    else:
        print("1")
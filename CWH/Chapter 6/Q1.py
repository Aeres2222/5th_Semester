a = int(input ("Enter your first number : "))
b = int(input ("Enter your second number : "))
c = int(input ("Enter your third number : "))
d = int(input ("Enter your fourth number : "))

if (a>d) :
    f1 = a
else :
    f1 = d

if (b>c) :
    f2 = b
else :
    f2 = c

if (f1>f2) :
    print(str(f1) +" : is the greates")
else :
    print(str(f2) +" : is the greates")
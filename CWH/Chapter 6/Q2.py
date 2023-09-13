a = int(input ("Enter your first subject marks : "))
b = int(input ("Enter your second subject marks : "))
c = int(input ("Enter your third subject marks : "))

if (a>33) :
    print("Pass in first subject")
else :
    print("Fail in first subject")

if (b>33) :
    print("Pass in Second subject")
else :
    print("Fail in Second subject")

if (c>33) :
    print("Pass in Third subject")
else :
    print("Fail in Third subject")

total = (a+b+c)/3

if (a>33 and b>33 and c>33 and total>40) :
    print("Overall pass")
else :
    print("Fail due to less than 40% ovarall marks")
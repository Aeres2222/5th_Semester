name = input ("What is your name good sir? : ") 
age = input ("What is your age good sir? : ")
weight = float(input ("What is your Weight good sir? : "))
networth = int(input ("Please specify your networth : "))
is_rich = networth>=100000
is_heavy = weight>=80

print ("Mr "+name)
print ("Age "+age)
print ("Are you HEAVY? : ",is_heavy)
print (str(weight),"KG")
print ("ARE YOU RICH? : ",is_rich)
print ("Networth = $",+networth)
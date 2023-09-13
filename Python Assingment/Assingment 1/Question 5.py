var1 = input("Enter the first variable: ")
var2 = input("Enter the second variable: ")

print(f"Original values: var1 = {var1}, var2 = {var2}")

temp = var1
var1 = var2
var2 = temp

print(f"Swapped values: var1 = {var1}, var2 = {var2}")
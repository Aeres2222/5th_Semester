decimal_number = int(input("Enter a decimal number: "))

binary_representation = bin(decimal_number)
octal_representation = oct(decimal_number)
hexadecimal_representation = hex(decimal_number)

print(f"Decimal: {decimal_number}")
print(f"Binary: {binary_representation}")
print(f"Octal: {octal_representation}")
print(f"Hexadecimal: {hexadecimal_representation}")
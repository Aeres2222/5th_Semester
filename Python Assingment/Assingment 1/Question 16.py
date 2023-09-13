start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
    return num == sum_of_digits

print(f"Armstrong numbers in the interval [{start}, {end}]:")
for num in range(start, end + 1):
    if is_armstrong(num):
        print(num)
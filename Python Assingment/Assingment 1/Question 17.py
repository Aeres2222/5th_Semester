n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_natural_numbers = (n * (n + 1)) // 2
    
    print(f"The sum of natural numbers from 1 to {n} is {sum_of_natural_numbers}")
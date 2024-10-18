def check_perfect(n):
    if n <= 1:
        return False
    
    sum_of_divisors = 0  # Initialize sum_of_divisors here

    # Find all divisors from 1 to n-1 and add them
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    # Return True if the sum of divisors equals the number, otherwise False
    return sum_of_divisors == n

# Get user input and call the function
number = int(input("Enter the number: "))
result = check_perfect(number)
print(f"Is the number perfect: {result}")


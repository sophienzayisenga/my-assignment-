def check_perfect(n):
    if n <= 1:
        return False
    
    sum_of_divisors = 0  

    
    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    
    return sum_of_divisors == n

print("Perfect numbers between 1 and 1,000,000 are:")
for number in range(1, 1000001):
    if check_perfect(number):
        print(number)

def check_prime(num):
    if num<=0:
       return False
    for i in range(2,int(num **0.5)+1):
        if num % i== 0:
          return False
    return True
def enter():
    while True:
       n=int(input("enter the positve number:"))
       if n <= 0:
          print("the number is not positeve")
       else:
           break
    print(f"the prime number of under or equal to {n} are:") 
    for num in range(2,n+1):
         if check_prime(num):
           print(num,end=" ")
enter()           

         
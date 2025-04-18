#Write a Python code that receives a number from the user and checks whether this number is prime.
#A prime number is a number greater than 1 that is only divisible by 1 and itself.
num = int   (input("Enter a number: "))
is_prime = True  #assume it is prime until we find a reason to say otherwise
if num <= 1:
    is_prime = False  #1 and any number below it is not prime
else:
    for i in range(2, int(num ** 0.5) + 1): #for i in range(2, num): check all the numbers between 2 and (num - 1) to see if any of them divide your number evenly
                                            #num ** 0.5 = square root of the number
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

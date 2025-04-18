#Write a Python program that takes a positive integer input from the user and calculates its factorial. Factorial is the product of all positive integers between a number itself and 1. 
#For example: if the user entered 5, the program should give the following output: Enter a number from the user: 5 Factorial: 120
num = int(input("Enter a number: "))  #int(..) converts the input to an integer
factorial = 1  #start with 1 because multiplying by 0 would make everything 0
for i in range(1, num + 1):   #Use a for loop to calculate factorial
    factorial *= i   #each loop multiplies the current factorial by i
    print("Factorial:", factorial)
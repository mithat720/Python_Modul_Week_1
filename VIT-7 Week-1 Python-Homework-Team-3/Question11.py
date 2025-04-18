#How to write a Python program that finds the largest of three numbers entered by a user?
num1 = float(input("Enter the first number: ")) #Use float() so it works with both integers and decimal numbers
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is: ", largest)


#largest = max(num1, num2, num3) Python also has a built-in function called max()
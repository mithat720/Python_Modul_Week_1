#Take a number input from the user and write a Python program that prints even numbers up to this number on the screen. Do this first with 'for' and then with 'while' loops.

# Ask the user for a number
num = int(input("Enter a number: "))

for i in range(1, num + 1):  #loops from 1 up to the number inclusive.
    if i % 2 == 0:  # checks if the number is divisible by 2
        print(i)


num = int(input("Enter a number: "))

i = 1 # starts counting from 1
while i <= num:
    if i % 2 == 0: # checks if it's even
        print(i)
    i += 1 # increases the counter each time
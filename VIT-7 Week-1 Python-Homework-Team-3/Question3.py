#Write a Python code that receives a start and end value from the user and prints all the numbers between these values ​​(including the end value) on the screen.
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))  # int(..) converts the input (a string) to a number

for i in range(start, end + 1):  # range() stops before the end number, so +1 includes the last number
    print(i) 
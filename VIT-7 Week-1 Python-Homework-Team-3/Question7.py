#How to create a loop that calculates the Fibonacci sequence and returns the result as a list containing numbers up to a certain limit?
limit = int(input("Enter a limit: "))
fib_list = [0, 1] #start with the first two Fibonacci numbers
while True:       #we use a while loop so we can keep generating numbers until we decide to stop.
    next_number = fib_list[-1] + fib_list[-2]   #this adds the last two numbers in the list to get the next one.
    if next_number > limit:
        break  #stop the loop if next number is over the limit
    fib_list.append(next_number)  #add it to the list
print("Fibbonacci sequence up to", limit, ":", fib_list)
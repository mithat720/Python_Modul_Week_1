#How to create a combination of loop and conditional statement that takes a word input from the user and checks whether that word is a palindrome (the same when read backwards)?
#A palindrome is a word (or phrase) that reads the same forwards and backwards. For example, the word "level" is a palindrome, but "hello" is not.
word = input("Enter a word: ")
reversed_word = word[::-1]
if word == reversed_word:
    print(f"{word} is a palindrome!") #f-string, the part inside {} will be evaluated and inserted into the string
else:
    print(f"{word} is not a palindrome.")
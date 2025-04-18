#Write a Python code that takes a word from the user and prints the reverse of this word on the screen.
word = input("Enter a word: ")
reversed_word = word[::-1] #reverse the word using slicing, word[::-1] gives you the word in reverse
print("Reversed word:", reversed_word)
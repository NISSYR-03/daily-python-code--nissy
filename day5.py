word = input("Enter a word: ")

if word == word[::-1]:
    print("This word is a PALINDROME")
else:
    print("This word is NOT a palindrome")

def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")
    
    # Check if the word is a palindrome
    if word == word[::-1]:
        return True
    else:
        return False

# Test the function
word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")

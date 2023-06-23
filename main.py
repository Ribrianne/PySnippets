import random
def is_palindrome(word):
    # Convert the word to lowercase and remove spaces
    word = word.lower().replace(" ", "")
    
    # Check if the word is a palindrome
    if word == word[::-1]:
        return True
    else:
        return False

def roll_dice():
    # Simulate rolling two dice
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    
    # Calculate the total
    total = dice_1 + dice_2
    
    # Print the result
    print(f"The dice rolled: {dice_1}, {dice_2}")
    print(f"Total: {total}")

# Roll the dice
roll_dice()

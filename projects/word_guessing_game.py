import random
import string

def display_hangman(tries):
    """Display hangman based on remaining tries"""
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |      
           |      
           |     
           -
        """
    ]
    return stages[tries]

def get_word():
    """Return a random word from the word list"""
    words = [
        'python', 'hangman', 'computer', 'programming', 'developer',
        'algorithm', 'database', 'network', 'security', 'keyboard',
        'monitor', 'application', 'function', 'variable', 'constant',
        'mathematics', 'science', 'knowledge', 'intelligence', 'adventure',
        'fantastic', 'wonderful', 'beautiful', 'chocolate', 'elephant',
        'butterfly', 'adventure', 'mystery', 'treasure', 'challenge'
    ]
    return random.choice(words).upper()

def display_board(guessed_letters, word):
    """Display the word with guessed letters and blanks"""
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter + ' '
        else:
            display += '_ '
    return display

def play_game():
    """Main game function"""
    print("\n" + "="*50)
    print("   WELCOME TO WORD GUESSING GAME!")
    print("="*50)
    
    word = get_word()
    guessed_letters = set()
    wrong_guesses = set()
    tries = 6
    
    print("\nI'm thinking of a word with", len(word), "letters.\n")
    print("You have", tries, "wrong guesses allowed.\n")
    
    while tries > 0:
        print(display_hangman(tries))
        print("\nWord: ", display_board(guessed_letters, word))
        print("Wrong guesses:", ', '.join(sorted(wrong_guesses)) if wrong_guesses else "None")
        print("Guessed letters:", ', '.join(sorted(guessed_letters - wrong_guesses)) if guessed_letters - wrong_guesses else "None")
        print(f"Tries remaining: {tries}\n")
        
        # Check if player won
        if all(letter in guessed_letters for letter in word):
            print("🎉 CONGRATULATIONS! You won! 🎉")
            print(f"The word was: {word}")
            return
        
        # Get player's guess
        guess = input("Guess a letter: ").upper()
        
        # Validate input
        if len(guess) != 1 or guess not in string.ascii_uppercase:
            print("❌ Please enter a single valid letter!\n")
            continue
        
        if guess in guessed_letters:
            print("❌ You already guessed that letter!\n")
            continue
        
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in word:
            print(f"✓ Good guess! '{guess}' is in the word!\n")
        else:
            print(f"✗ Sorry! '{guess}' is not in the word!\n")
            wrong_guesses.add(guess)
            tries -= 1
    
    # Player lost
    print(display_hangman(tries))
    print("\n😞 GAME OVER! You lost!")
    print(f"The word was: {word}")

def main():
    """Main function to run the game"""
    while True:
        play_game()
        
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋\n")
            break

if __name__ == "__main__":
    main()

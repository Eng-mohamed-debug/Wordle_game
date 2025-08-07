# 1- get suitable library that contains words
# 2- get suitable library to print colors in console
# 3- getting the words ready
# 4- making the welcome screen
# 5- rules screen
# 6- game play screen and logic
import random
from english_words import get_english_words_set
import colorama
colorama.init(autoreset=True)






def get_word():
    words = list(get_english_words_set(['web2'], lower=True))
    words = [word for word in words if len(word) == 5 and word.isalpha()] # get just a word with len 5
    return random.choice(words).lower()



def game():
    # 1- we get the word
    # 2- we initialize no_tries
    # 3- take the guess from the user and show the available tries
    # 4- feedback logic (colors)


    target_word = get_word() # step 1
    no_tries = 6  # step 2
    word_length = 5
    guessed = False # I will use it to stop the game if the player done

    print("\n🎮 Game started! Guess the 5-letter word:\n")

    # step 3
    while no_tries > 0:
        guess = input(f"{7-no_tries}/6 tries available: ").lower() # convert it to lower case to compare
        # check that user doesn't enter a number
        if len(guess) != word_length or not guess.isalpha():
            print(colorama.Fore.RED + "❌ Please enter a valid 5-letter word.\n")
            continue

        if guess == target_word:
            print(colorama.Fore.GREEN + "\n🎉 Correct! You’ve guessed the word!\n")
            guessed = True
            break

        # step 4 (colors logic)
        feedback = ""
        for i in range(word_length):
            if guess[i] == target_word[i]:
                feedback += colorama.Fore.GREEN + guess[i].upper()
            elif guess[i] in target_word:
                feedback += colorama.Fore.YELLOW + guess[i].upper()
            else:
                feedback += colorama.Fore.LIGHTBLACK_EX + guess[i].upper()
        print("Feedback:", feedback + colorama.Fore.RESET + "\n")

        no_tries -= 1

        if not guessed and no_tries == 0:
            print(colorama.Fore.RED + f"\n💀 Out of tries! The word was: {target_word.upper()}\n")







def main():
    greet()
    show_menu()
    while True:
        choice = input("Enter your choice (1-3): ").strip()
        if choice == '1':
            display_rules()
            show_menu()
        elif choice == '2':
            game()
            show_menu()
        elif choice == '3':
            print(colorama.Fore.MAGENTA + "\n👋 Thanks for playing! Goodbye!\n")
            break
        else:
            print(colorama.Fore.RED + "❌ Invalid choice. Try again.\n")















def greet():
    welcome_word = r"""
+--------------------------------------------------------------------------+
|                                                                          |
|  __        __     _                                _                     |
|  \ \      / /___ | |  ___  ___   _ __ ___    ___  | |_  ___              |
|   \ \ /\ / // _ \| | / __|/ _ \ | '_ ` _ \  / _ \ | __|/ _ \             |
|    \ V  V /|  __/| || (__| (_) || | | | | ||  __/ | |_| (_) |            |
|     \_/\_/  \___||_| \___|\___/ |_| |_| |_| \___|  \__|\___/             |
|  __        __               _  _          ____                           |
|  \ \      / /___   _ __  __| || |  ___   / ___|  __ _  _ __ ___    ___   |
|   \ \ /\ / // _ \ | '__|/ _` || | / _ \ | |  _  / _` || '_ ` _ \  / _ \  |
|    \ V  V /| (_) || |  | (_| || ||  __/ | |_| || (_| || | | | | ||  __/  |
|     \_/\_/  \___/ |_|   \__,_||_| \___|  \____| \__,_||_| |_| |_| \___|  |
|                                                                          |
+--------------------------------------------------------------------------+
"""
    print(colorama.Fore.RED + welcome_word)



def display_rules():
    rules = r"""
╔══════════════════════════════════════════════════════════════════════════╗
║                             HOW TO PLAY WORDLE                           ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║ 1. OBJECTIVE: Guess the hidden 5-letter word in 6 attempts.              ║
║                                                                          ║
║ 2. AFTER EACH GUESS:                                                     ║
║    • 🟢 Green   = Correct letter in the correct position.                ║
║    • 🟡 Yellow  = Correct letter but in the wrong position.              ║
║    • ⬜ Gray     = Letter not in the word at all.                        ║
║                                                                          ║
║ 3. EXAMPLE:                                                              ║
║    Hidden word: "CRANE"                                                  ║
║    Your guess: "CRATE" → 🟢🟢🟢⬜🟢 (E is misplaced)                    ║
║                                                                          ║
║ 4. TIPS:                                                                 ║
║    • Use process of elimination based on feedback.                       ║
║    • Common letters (E, A, R, T) are good starting points.               ║
║                                                                          ║
║ 5. Press ENTER to submit your guess.                                     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
    print(colorama.Fore.CYAN + rules)






def show_menu():
    menu = r"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║    ███╗   ███╗ █████╗ ██╗███╗   ██╗    ███████╗██╗ ██████╗███████╗██████╗ ║
║    ████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██║██╔════╝██╔════╝██╔══██╗║
║    ██╔████╔██║███████║██║██╔██╗ ██║    █████╗  ██║██║     █████╗  ██████╔╝║
║    ██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██╔══╝  ██║██║     ██╔══╝  ██╔══██╗║
║    ██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ██║     ██║╚██████╗███████╗██║  ██║║
║    ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝    ╚═╝     ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝║
║                                                                          ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                          ║
║                           1. 📜 Show Rules                               ║
║                           2. 🎮 Play Game                                ║
║                           3. 🚪 Exit                                     ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""
    print(colorama.Fore.YELLOW + menu)










if __name__ == "__main__":
    main()
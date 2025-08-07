# 1- get suitable library that contains words
# 2- get suitable library to print colors in console
# 3- getting the words ready
# 4- making the welcome screen
# 5- rules screen
# 6- game play screen and logic
from random import sample
from english_words import get_english_words_set
import colorama
colorama.init(autoreset=True)






def get_words():
    words = list(get_english_words_set(['web2'], lower=True))
    words = sample(words, 5)
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return words



def main():
    greet()
    show_menu()














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
import random
import words
from colorama import Fore, Style
import colorama
colorama.init()


def print_word(word, prizn):
    for el in range(5):
        if prizn[el] == "G":
            print(Fore.GREEN + word[el] + Style.RESET_ALL, end = " ")
        elif prizn[el] == "Y":
            print(Fore.BLUE + word[el] + Style.RESET_ALL, end = " ")
        else:
            print(Fore.RED + word[el] + Style.RESET_ALL, end = " ")
    


def main():
    wrong_answers = 0
    answer = random.choice(words.wordsfor)
    
    while wrong_answers <= 5:
        word = ["_"]* len(answer)
        prizn = ["B"] * 5
        print(f"You have {6 - wrong_answers} tries")
        
        write = True
        while write:
            guess = input("Try choose word (5 letters) : ").lower()
            if not guess.isalpha() or len(guess) != 5:
                print("Incorrect input")
                continue
            else:
                write = False
        
        for i in range(5):
            if guess[i] in answer:
                prizn[i] = "Y" 
                word[i] = guess[i]
            if guess[i] == answer[i]:
                prizn[i] = "G" 
                word[i] = guess[i]
        print_word(word, prizn)
        if all(el == "G" for el in prizn):
            print()
            print("Congratulations! You are win!")
            print(f"It was word: {answer}")
            break
        elif wrong_answers == 5:
            print()
            print("You are loose!")
            print(f"It was word: {answer}")
        wrong_answers += 1
        print()
        
                
                


if __name__ == "__main__":
    main()











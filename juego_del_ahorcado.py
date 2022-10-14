import os
import random


def get_word():
    with open("./archivos/data.txt", "r", encoding = "utf-8") as f:
        word = random.choice(f.readlines())
        return word.replace(' ', '').rstrip("\n").upper()


def check_letter(word, letters):
    letter_list = ['_' if i not in letters else i for i in word]
    print(f"""\n\n      {letter_list} \n""")
    if '_' not in letter_list:
        print(f"""    You did !    """)
        return True
    else:
        return False


def get_lives(word, letters):
    lives = len(word) * 2 - len(letters)
    print(f"""\n     You have: {lives} lives \u2764\uFE0F ! \n""")
    return True if lives > 0 else False


def get_letter(letters):
    try:
        letter = input("  Please, Give a letter: ")
        if letter.isnumeric():
            raise ValueError
        letters.append(letter.replace(' ', '').upper())
        os.system('clear')
        return letters
    except ValueError:
        os.system('clear')
        print("Just letters!")


def game():
    word = get_word()
    letters = []

    while not check_letter(word, letters):
        have_lives = get_lives(word, letters)
        if have_lives: 
            get_letter(letters)
        else:
            os.system('clear')
            print("\n         you lost the game, try again")
            break


def run():
    game()
        
    
if __name__ == '__main__':
    run()

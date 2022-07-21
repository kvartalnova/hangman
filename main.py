import random


words = ['слон', 'жираф', 'дельфин', 'горилла', 'попугай']
word = list(random.choice(words))
db = []
attempt = 0

def input_user_letter():
    return input("\nвведите букву: ")

def check_letter(letter):
    if letter in word:
        add_letter_db(letter)
    else:
        global attempt
        attempt += 1
        show_attempt_status()

def add_letter_db(arg_letter):
    db.append(arg_letter)

def show_attempt_status():
    print(f'у тебя осталось {10 - attempt} попыток!')

def create_guessed_part():
    result = []
    for let in word:
        if let in db:
            result.append(let)       
        else:
            result.append('*')
    return result

def print_result_guessed_word(guessed_part):
    print('результат: ' + ''.join(guessed_part))

def print_success_word():
    print('ты выйграл, молодец!')

def print_unsucces_word():
    print('ты проиграл ;(')


print('*' * len(word))
while attempt < 10:

    letter = input_user_letter()
    check_letter(letter)
        
    guessed_part = create_guessed_part()
    print_result_guessed_word(guessed_part)

    if guessed_part == word:
        print_success_word()
        break
        
else:
    print_unsucces_word()

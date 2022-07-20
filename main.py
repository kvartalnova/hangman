import random


words = ['слон', 'жираф', 'дельфин', 'горилла', 'попугай']
word = list(random.choice(words))
db = []
attemp = 0

print('*' * len(word))
while attemp < 10:
    letter = input('\nвведите букву: ')

    if letter in word:
        db.append(letter)
    
    else:
        attemp += 1
        print(f'у тебя осталось {10 - attemp} попыток!')
    
    result = []

    for let in word:

        if let in db:
            result.append(let)
        
        else:
            result.append('*')
    
    print('результат: ' + ''.join(result))
    if result == word:
        print('молодец!')
        break
        
else:
    print('ты проиграл!')
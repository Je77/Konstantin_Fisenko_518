import random

print("""H A N G M A N
The game will be available soon.""")
try_words = []
vse_bukvi = []
life = 8
words = ['python', 'java', 'kotlin', 'javascript']
random_word = random.choice(words)
b = '-' * (len(random_word))
random_word = list(random_word)
random_word_set = set(random_word)
while True:
    answer = input('Type "play" to play the game, "exit" to quit: ')
    if answer == 'play':
        while life != 0:
            letter = input((f"""
        H A N G M A N
        Guess the word:"""))
            if len(letter) != 1:
                print('You should print a single letter')
                print(life)
            elif letter not in ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                                'o', 'p', 'q', 'r', 's',
                                't', 'u', 'v', 'w', 'x', 'y', 'z']:
                print('It is not an ASCII lowercase letter')
                print(life)
            elif letter in try_words:
                print('No improvements')
                life -= 1
                print(life)
            elif letter in random_word:
                print(life)


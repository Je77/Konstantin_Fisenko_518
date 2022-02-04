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
        


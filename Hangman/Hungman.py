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

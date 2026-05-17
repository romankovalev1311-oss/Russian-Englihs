import random

glasses = 0

words_by_level = {
    "easy": ["кот", "собака", "яблоко", "молоко", "солнце"],
    "medium": ["банан", "школа", "друг", "окно", "жёлтый"],
    "hard": ["технология", "университет", "информация", "произношение", "воображение"]
}

words_by_english = {
    "easy": ["cat", "dog", "apple", "milk", "sun"],
    "medium": ["banana", "school", "friend", "window", "yellow"],
    "hard": ["technology", "university", "information", "pronunciation", "imagination"]
}

word = random.choice(words_by_level["easy"])
word = random.choice(words_by_level["medium"])
word = random.choice(words_by_level["hard"])

print(word)

if word == "easy":
    words_by_english = input('Введите слово на английском')
elif word == words_by_english:
    glasses = +10
else:
    glasses = -10

if word == "medium":
    words_by_english = input('Введите слово на английском')
elif word == words_by_english:
    glasses = +10
else:
    glasses = -10

if word == "hard":
    words_by_english = input('Введите слово на английском')
elif word == words_by_english:
    glasses = +10
else:
    glasses = -10

print('У вас', glasses, 'очков')

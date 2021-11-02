import random
import nltk
from nltk.tokenize import WhitespaceTokenizer
from collections import defaultdict, Counter


def sentence(dictionary):
    while True:
        words = random.choice(list(dictionary.keys())).split(' ')
        if words[0][0].isupper() and words[0][-1] not in '.?!':
            break
    sent = ' '.join(words)

    while True:
        tail = list(dictionary[' '.join(words)].keys())
        count = list(dictionary[' '.join(words)].values())

        if len(tail) > 1:
            next_word = random.choices(tail, count)[0]
        elif len(tail) == 0:
            sent = sentence(dictionary)
            break
        else:
            next_word = list(dictionary[' '.join(words)].keys())[0]

        sent = sent + ' ' + next_word
        words = [words[1], next_word]

        if next_word[-1] in '.?!' and len(sent.split(' ')) >= 5:
            break

    return sent


corpus = input()
wt = WhitespaceTokenizer()

with open(f"{corpus}", "r", encoding="utf-8") as f:
    tokens = wt.tokenize(f.read())

tri = list(nltk.trigrams(tokens))
temp_dict = defaultdict(list)
dict_of_tri = defaultdict(dict)

for t in tri:
    temp_dict[str(t[0] + ' ' + t[1])].append(t[2])

for head, tails in temp_dict.items():
    f_counter = Counter(tails)
    dict_of_tri[head] = f_counter

for pseudo_sentence in range(10):
    print(sentence(dict_of_tri))

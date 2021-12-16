from __future__ import print_function
import random

setone = ('air', 'fly', 'bus', 'test', 'pie', 'apple', "phone")
settwo = ('visual', 'studio', 'python', 'airbus')
setthree = ('laptop', 'keyboard', 'lamp')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_phrase():
    buzz_terms = sample(setone, 2)
    phrase = ' '.join([sample(setone), buzz_terms[0], sample(settwo), sample(setthree)])
    return phrase.title()

if __name__ == "__main__":
    print(generate_phrase())

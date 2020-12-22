import argparse 
from functools import reduce


def get_letters():
    with open('千字文.txt') as fp:
        verse = fp.read()
    letters = [l for l in verse if l != '\n' if l != ' ']
    return(letters)


def to_decimal(letters):
    VERSE=get_letters()
    v = reduce(lambda x,y:x+y , [
        (VERSE.index(l)+1) * (1000 ** i) 
        for i, l in enumerate(reversed(letters))
    ])
    return v


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='1000decimal decoder.')
    parser.add_argument('words', metavar='words', type=str, help='Input 1000decimal')
    args = parser.parse_args()
    words = args.words
    try:
        print(f"{words} => {to_decimal(words)}")
    except ValueError:
        print(f"{words} includes out-of-scope characters.")
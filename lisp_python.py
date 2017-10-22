# Peter Norvig's simple random sentence generator

from random import choice

grammar = dict(
    S = [['NP', 'VP']],
    NP = [['Art', 'N']],
    VP = [['V', 'NP']],
    Art = ['the', 'a'],
    N = ['man', 'ball', 'woman', 'table'],
    V = ['hit', 'took', 'saw', 'liked'],
)

def generate(phrase):
    if isinstance(phrase, list):
        return mappend(generate, phrase)
    elif phrase in grammar:
        return generate(choice(grammar[phrase]))
    else:
        return [phrase]

def generate_tree(phrase):
    if isinstance(phrase, list):
        return map(generate_tree, phrase)
    elif phrase in grammar:
        return [phrase] + generate_tree(choice(grammar[phrase]))
    else: return [phrase]

def mappend(fn, args):
    return [item for result in map(fn, args)
            for item in result]

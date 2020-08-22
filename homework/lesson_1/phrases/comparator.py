from typing import Dict

_results: Dict[int, str] = {
    0: 'Фраза 1 длиннее фразы 2',
    1: 'Фраза 2 длиннее фразы 1',
    2: 'Фразы равной длины'
}


def compare(phrase_1, phrase_2):
    first = len(str(phrase_1))
    second = len(str(phrase_2))

    if first > second:
        print(_results[0])
    elif second > first:
        print(_results[1])
    else:
        print(_results[2])

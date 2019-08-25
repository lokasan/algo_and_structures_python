"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


string = list('bill piu will')
freq = Counter(string)
freq = deque(sorted(freq.items(), key=lambda symbol: symbol[1]))

if len(freq) != 1:
    while len(freq) > 1:
        wt = freq[0][1] + freq[1][1]
        save = {0: freq.popleft()[0],
                1: freq.popleft()[0]}
        for i, c in enumerate(freq):
            if wt > c[1]:
                continue
            else:
                freq.insert(i, (save, wt))
                break
        else:
            freq.append((save, wt))
else:
    wt = freq[0][1]
    save = {0: freq.popleft()[0], 1: None}
    freq.append((save, wt))

haffman_code(freq[0][0])
for i in string:
    print(code_table[i], end=" ")

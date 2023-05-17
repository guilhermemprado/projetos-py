import itertools

string = input('Text a ser permutada: ')

result = itertools.permutations(string, len(string))

for i in result:
    print(''.join(i))
import itertools

n = 5
blah = []

for i in range(n):
    blah.append(i+1)

x = list(itertools.permutations(blah))

print(len(x))

for a in x:
    for b in a:
        print(b, end=' ')
    print('\n')

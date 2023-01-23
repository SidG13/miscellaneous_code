with open('rosalind_revc.txt') as file:
    stuff = list(file.read())

dna = list(stuff[::-1])

for x in range(len(dna)):
    if dna[x] == 'A':
        dna[x] = 'T'
    elif dna[x] == 'T':
        dna[x] = 'A'
    if dna[x] == 'C':
        dna[x] = 'G'
    elif dna[x] == 'G':
        dna[x] = 'C'

print(''.join(dna))
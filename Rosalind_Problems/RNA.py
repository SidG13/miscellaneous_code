with open('rosalind_rna.txt') as file:
    rna = list(file.read())

print(rna)
for x in range(len(rna)):
    if rna[x] == 'T':
        rna[x] = 'U'
print(''.join(rna))
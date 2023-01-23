countA = 0
countC = 0
countG = 0
countT = 0

with open('rosalind_dna.txt') as file:
    s = file.read()

for x in s:
    if x == 'A':
        countA += 1
    if x == 'C':
        countC += 1
    if x == 'G':
        countG += 1
    if x == 'T':
        countT += 1

print(countA, countC, countG, countT)
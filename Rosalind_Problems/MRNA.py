codon_table = {'A': 4,               'R': 6,
               'N': 2,               'D': 2,
               'C': 2,               'Q': 2,
               'E': 2,               'G': 4,
               'H': 2,               'I': 3,
               'L': 6,               'K': 2,
               'M': 1,               'F': 2,
               'P': 4,               'S': 6,
               'T': 4,               'W': 1,
               'Y': 2,               'V': 4}


protein_seq = ''

comb = 1
for a in protein_seq:
    comb = codon_table[a] * comb
print((comb*3) % 1000000)

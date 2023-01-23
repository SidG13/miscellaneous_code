import requests
import re

protein_list = []  # Make empty list
with open('rosalind_mprt.txt') as file:
    for line in file:
        protein_list.append(line.strip('\n'))  # Put proteins in list, with newlines removed.


for protein in protein_list:
    data = requests.get('http://www.uniprot.org/uniprot/{}.fasta'.format(protein))  # Gets HTTP FASTA document

    x = data.text  # Converts FASTA to type 'str'
    protein_seq = (''.join(x.split('\n')[1:]))  # split at newlines, put into list. Take all but first line, join into str.

    print(protein)
    for a in re.finditer('N(?=[^P][(S|T)][^P])', protein_seq):  # Returns iterator using REGEX pattern (N-glycosylation motif)
            print(a.span()[1], end=' ')  # Get the 2nd element of .span tuple (end pt. of the match).
    print('\n')

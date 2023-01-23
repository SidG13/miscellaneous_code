with open('rosalind_gc.txt', 'r') as file:
    fasta = file.read()


rough_list = fasta.split('>')

list_of_ids = []
list_of_sequences = []

for seq in rough_list:
    seq_id = seq[:14]
    list_of_ids.append(seq_id.replace('\n',''))
    sequence = seq[14:]
    list_of_sequences.append(sequence.replace('\n',''))
del (list_of_ids[0])
del (list_of_sequences[0])


list_of_scores = []

hiScore = 0
hiID = ''
for s in list_of_sequences:
    gcCounter = 0
    for base in s:
        if base == 'G':
            gcCounter += 1
        if base == 'C':
            gcCounter += 1
    list_of_scores.append((gcCounter / len(s)) * 100)

index = list_of_scores.index(max(list_of_scores))
print(list_of_ids[index])
print(list_of_scores[index])






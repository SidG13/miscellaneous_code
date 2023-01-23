import re

with open('rosalind_lcsm.txt') as file:
    data = file.read()

#  Boring data cleaning
cleaner_data = data.replace('\n', '').split('>')
del cleaner_data[0]
seq_list = []
for stuff in cleaner_data:
    temp = re.findall('^Rosalind_[0-9]*(\S*)', stuff)
    seq_list += temp
smallest_seq = (min(seq_list))
seq_list.remove(smallest_seq)


#  Completely substring the smallest sequence, store all subsequences in list
temp = []
for i in range(len(smallest_seq)):
    for j in range(i+1, len(smallest_seq)):
        temp.append((smallest_seq[i:j+1]))
substring_list = (sorted(temp, key=len))


#  Check if each substring is in each sequence, if so put it into a list. If not break the loop (save time)
#  Find the max (len) of the type 'set' list.
temp_list = []
for substring in substring_list:
    for seq in seq_list:
        if substring not in seq:
            break
        else:
            temp_list.append(substring)
print(max(set(temp_list), key=len))



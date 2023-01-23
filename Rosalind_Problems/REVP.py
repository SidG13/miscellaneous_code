import re
string = 'TCAATGCATGCGGGTCTATATGCAT'


def reverse_complementation(something):
    complement = ''
    for a in something:
        if a == 'A':
            complement += 'T'
        if a == 'T':
            complement += 'A'
        if a == 'C':
            complement += 'G'
        if a == 'G':
            complement += 'C'
    return complement[::-1]  # return complement in reverse

# Completely substring string, sort by length, store in list
temp = []
for i in range(len(string)):
    for j in range(i+1, len(string)):
        temp.append((string[i:j+1]))
substring_list = (sorted(temp, key=len))


# Collect those substrings of the correct length in list
real_substrings = []
for b in substring_list:
    if 4 <= len(b) <= 12:
        real_substrings.append(b)

#  Take the usable substrings and get their reverse complements
reversals = []
for z in real_substrings:
    reversals.append(reverse_complementation(z))


#  If a substring equals its reverse complement, its a restriction site. Collect those substrings.
restriction_sites = []
for i in range(len(real_substrings)):
    if real_substrings[i] == reversals[i]:
        restriction_sites.append(real_substrings[i])


def output_maker():
    for x in restriction_sites:
        for m in re.finditer(x, string):
            print(m.start()+1, len(x))


output_maker()

#  I used an online duplicate line remover to clean the data, sorry!
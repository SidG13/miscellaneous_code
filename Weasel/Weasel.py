import random

childNumber = 100
mut_rate = 0.05
ref_string = "METHINKS*IT*IS*LIKE*A*WEASEL"


# make the first random string
histring = ''
for i in range(len(ref_string)):
    char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ*")
    histring += char
print(histring)
print("---------------")


# score children
def fitness_score(string2):
    return sum(100*((a == b)/(len(ref_string))) for a, b in zip(string2, ref_string))


# mutate any string a set number of times. Record the highest scoring string and its score
def str_mutator(string):
    hiscore = 0
    for j in range(1, childNumber):
        copy = list(string)
        for c in range(len(copy)):
            char = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ*")
            if random.random() < mut_rate:
                copy[c] = char
            string3 = ''.join(copy)
        if fitness_score(string3) > hiscore:
            hiscore = fitness_score(string3)
            histring = string3
    print("---------------")
    print(histring, hiscore)
    return histring


counter = 0
while histring != ref_string:
    histring = str_mutator(histring)
    counter += 1
print("Number of generations was " + str(counter))

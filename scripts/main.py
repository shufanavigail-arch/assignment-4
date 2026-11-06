import random
def seq_generator(list, needed):
    seq = ''
    for i in range(int(needed)):
        rand = random.randint(0, len(list)-1)
        seq = seq + list[rand]
    return seq


file = open("results/Out_RandProtSeq.txt", "w")
non_polar = ['M', 'A', 'V', 'L', 'I', 'P', 'F', 'W', 'G', 'C']
polar = ['N', 'Q', 'S', 'T', 'Y']
positive = ['K', 'R', 'H']
negative = ['D', 'E']
seq_len = 150
non_polar_needed = seq_len*0.5 - 1
polar_needed = seq_len*0.3
positive_needed = seq_len*0.1
negative_needed = seq_len*0.1
seq_num = int(input('Please indicate how many random protein sequences you need (1-1000)? '))
for i in range(seq_num):
    seq = ''
    for j in range(seq_len):
        seq = seq + non_polar[0] 


import random
def seq_generator(list, needed): #function that creats a list of amino acids based on their chemical property and the needed length of the sequence of that specific property.
    seq = []
    for i in range(int(needed)): #loop that runs the number of times needed to create a sequence of the specified length.
        rand = random.randint(0, len(list)-1) #randomly selects an index from the list of amino acids
        seq.append(list[rand])
    return seq

#files
file = open("results/Out_RandProtSeq.txt", "w")
#amino acid lists
non_polar = ['M', 'A', 'V', 'L', 'I', 'P', 'F', 'W', 'G', 'C']
polar = ['N', 'Q', 'S', 'T', 'Y']
positive = ['K', 'R', 'H']
negative = ['D', 'E']
#variables
seq_len = 150
non_polar_needed = seq_len*0.5 - 1
polar_needed = seq_len*0.3
positive_needed = seq_len*0.1
negative_needed = seq_len*0.1
#input
seq_num = int(input('Please indicate how many random protein sequences you need (1-1000)? '))

for i in range(seq_num):#loop that runs the number of times the user specified.
    seq = []
    #used the function seq_generator to create a list of each chemical property of the amino acids, then added them together to creat a list of all the amino acids in the sequence created.
    seq = seq_generator(non_polar, non_polar_needed) + seq_generator(polar, polar_needed) + seq_generator(positive, positive_needed) + seq_generator(negative, negative_needed)
    random.shuffle(seq) #randomly shuffles the list of amino acids to create a random sequence of amino acids.
    seq = ([non_polar[0]] + seq) #adds a methionine to the start of the sequence.
    file.write('>Rand_Prot' + str(i+1) + '\n') #writes the header for the sequence in the results file.
    file.write(''.join(seq) + '\n') #converts the list to a string and writes the sequence of amino acids to the results file.

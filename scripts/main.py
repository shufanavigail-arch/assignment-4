import random
def seq_generator(list, needed): #function that creats a list of amino acids based on their chemical property and the needed length of the sequence of that specific property.
    seq = []
    for i in range(int(needed)): #loop that runs the number of times needed to create a sequence of the specified length.
        rand = random.randint(0, len(list)-1) #randomly selects an index from the list of amino acids
        seq.append(list[rand])
    return seq

def check_input(seq_num): #function that checks if the input is valid.
    if seq_num >= 1 and seq_num <= 1000: #checks if the input is within the specified range.
        return True
    else:
        return False

def validate_output(seq): #function that checks if the output is valid.
    non_polar_count = 0
    polar_count = 0
    positive_count = 0
    negative_count = 0
    for aa in seq: #loop that counts the number of each type of amino acid in the sequence.
        if aa in non_polar:
            non_polar_count += 1
        elif aa in polar:
            polar_count += 1
        elif aa in positive:
            positive_count += 1
        elif aa in negative:
            negative_count += 1
    non_polar_count -= 1 #subtracts 1 from the non_polar_count to account for the methionine added to the start of the sequence.
    if non_polar_count == non_polar_needed and polar_count == polar_needed and positive_count == positive_needed and negative_count == negative_needed and seq[0] == 'M' and len(seq) == 150: #checks if the sequence meets the requirements.
        return True
    else:
        return False


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
seq_num = 0
while not check_input(seq_num): #loop that runs until the user inputs a valid number.
    try:
        seq_num = int(input('Please indicate how many random protein sequences you need (1-1000)? '))
    except ValueError:
        print('Please enter a valid number.')
    if not check_input(seq_num):
        print('Please enter a number between 1 and 1000.')

for i in range(seq_num):#loop that runs the number of times the user specified.
    seq = []
    #used the function seq_generator to create a list of each chemical property of the amino acids, then added them together to creat a list of all the amino acids in the sequence created.
    seq = seq_generator(non_polar, non_polar_needed) + seq_generator(polar, polar_needed) + seq_generator(positive, positive_needed) + seq_generator(negative, negative_needed)
    random.shuffle(seq) #randomly shuffles the list of amino acids to create a random sequence of amino acids.
    seq = ([non_polar[0]] + seq) #adds a methionine to the start of the sequence.
    file.write('>Rand_Prot' + str(i+1) + '\n') #writes the header for the sequence in the results file.
    file.write(''.join(seq) + '\n') #converts the list to a string and writes the sequence of amino acids to the results file.

    print(validate_output(seq)) #prints the output of the validate_output function to check if the sequence meets the requirements expected.

file.close() #closes the results file.
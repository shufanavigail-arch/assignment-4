This program generates protein sequences (1-1000 sequences, depending on the
number the user chooses). Each sequence begins with the amino acid 
Methionine (M), and the rest of the amino acids position is random.
The sequence is made of exactly 150 amino acids.

The protein sequence must include 50% non-polar amino acids, 30% polar amino
acids, 10% positive amino acids and 10% negative amino acids.

The main program, where you run the code is a file called "main.py", 
it's in the scripts folder. 

The programs output is in the file 'Out_RandProtSeq.txt'. The output 
is all the generated protein sequences.

code description:

The code has three functions:

Function 1 - seq_generator
Function 1 is used to generate a list of randomly picked amino acids in
each chemical property. The output is that same list.
The input is a list and a number. it picks an item from the list randomly
for n times (n - the input number), and by that creates a new list made of items
from the list and whos length is the input number.

Function 2 - check_input
The input is an integer. It checks whether the integer is between 1-1000, 
which is the required range of the number of sequences generated.
It is used to check that the user entered a valid sequence number. 
The output is 'True' if its valid and 'False' if its not.

Function 3 - validate_output
The input is a list. It checks whether the list is valid
(If the sequnce begins with Methionine, its total length is 150,
and that the number needed of each amino acid chemical property
is what it should be).

There are lists of each amino acid group with different chemical property
(polar, non-polar, positive, and negative amino acids).
Then, the number needed of each amino acid type is calculated 
(based on the amino acids' type percent as stated in the beggining of the 
README file, and the sequences' length)
The user is asked to input the number of sequences to generate.
Function 2 is then used to check if the users' input is valid, if its not it 
prints what is wrong with the sequence, and enables the used to type another input.
If the users' input is valid, a loop in the length of the number they entered
runs. In this loop, function 1 is used to generate lists of all the different
amino acid groups, then it adds the lists together and converts them into a string.
It writes the results into the output file, and uses function 3 to check
if each sequence is valid.


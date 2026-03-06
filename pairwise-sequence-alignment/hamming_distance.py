##### What is Hamming Distance? #####
# Process which calculates the number of positions at which the corresponding symbols are different between two sequences. 
# It is a measure of the dissimilarity between two sequences and is commonly used in bioinformatics to compare DNA, RNA, or protein sequences. 
# The hamming function from skbio takes two sequences as input and returns the hamming distance between them.


# Lets see how hamming distance works w/o using skbio package
def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2):
        raise ValueError("Sequences must be of equal length")
    else:
        count = 0
        for i in range(len(seq1)):
            if seq1[i] != seq2[i]:
                count += 1
                print(f"Position {i}: {seq1[i]} != {seq2[i]}")
        return count
    
seq1 = "AGCTAGCTGAAGT"
seq2 = "AGCTTGCAGTTGA"
print(f"Hamming distance between {seq1} and {seq2} is: {hamming_distance(seq1, seq2)}")


# Calulating hamming distance using skbio package. 
# this calculates more of a percentage of the distance rather than the actual number of positions that are different.
from skbio import DNA
from skbio.sequence.distance import hamming 

seq1 = DNA("AGCTAGCTGAAGT")
seq2 = DNA("AGCTTGCAGTTGA")
print(f"Hamming distance between {seq1} and {seq2} is: {hamming(seq1, seq2)}")  




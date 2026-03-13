#reading the DNA sequence from a file 
file_path = './FASTA/hemoglobin-subunit-beta.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read()

# creating a complementry RNA sequence strand from the DNA sequence strand
# this does the mappling like this: A -> U, T -> A, C -> G, G -> C
def complementry_rna(dna_seq):
    translation_tb  = dna_seq.maketrans('ATCG', 'UAGC') #maketrans() method is used to create a translation table that maps each character in the first string ('ATCG') to the corresponding character in the second string ('UAGC'). This allows us to easily translate the DNA sequence into an RNA sequence by replacing 'A' with 'U', 'T' with 'A', 'C' with 'G', and 'G' with 'C'.
    complement_rna = dna_seq.translate(translation_tb) #translate() method is used to perform the actual translation of the DNA sequence into an RNA sequence using the translation table created by maketrans(). It replaces each character in the DNA sequence according to the mapping defined in the translation table, resulting in the corresponding RNA sequence.
    return complement_rna

comp_rna_strand = complementry_rna(dna_sequence)
print("The complementry RNA Sequence Strand is: " + "\n\n" + comp_rna_strand)


# transcribing the DNA sequence to RNA sequence by replacing 'T' with 'U'
def transcribe_dna_to_rna(dna_seq):
    rna_seq = dna_seq.replace('T', 'U')
    return rna_seq

rna_sequence = transcribe_dna_to_rna(dna_sequence)
print("The transcribed RNA Sequence is: " + "\n\n" + rna_sequence)


### translating the RNA sequence to protein sequence ###
# copy the dictionary from the rna_codon_table.txt file 
RNA_Codons = {
    # 'M' - START, '*' - STOP
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UGU": "C", "UGC": "C",
    "GAU": "D", "GAC": "D",
    "GAA": "E", "GAG": "E",
    "UUU": "F", "UUC": "F",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G",
    "CAU": "H", "CAC": "H",
    "AUA": "I", "AUU": "I", "AUC": "I",
    "AAA": "K", "AAG": "K",
    "UUA": "L", "UUG": "L", "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUG": "M",
    "AAU": "N", "AAC": "N",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "CAA": "Q", "CAG": "Q",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R", "AGA": "R", "AGG": "R",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S", "AGU": "S", "AGC": "S",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UGG": "W",
    "UAU": "Y", "UAC": "Y",
    "UAA": "*", "UAG": "*", "UGA": "*"
}

new_rna_sequence = rna_sequence.replace("\n", "").replace(" ", "").strip()

### the below is a short sample to test it out coz, its not too long ###
#new_rna_sequence = "AUG ACG GGA CAC ACC ACU CCG GGA CCC GUC CAA CCA UAG UUC CAA UGU AUG GUC UGA AUU CCU CUG GUU AUC UUU GAC CC"
#                    M   T   G   H   T   T   P   G   P   V   Q   P   *   F   Q   C   M   V   *   I   P   L   V   I   F   D
#new_rna_sequence = "AUGACGGGACACACCACUCCGGGACCCGUCCAACCAUAGUUCCAAAUGUCUGUCUGAAUUCCUCUGGUUAUCUUUGACCC"

def rna_to_protein(rna_seq):
    protein_seq = ""
    start_codon = "AUG"
    start_codon_position = rna_seq.index(start_codon)
    for i in range(start_codon_position, len(rna_seq), 3):
        codon = rna_seq[i:i+3]
        if len(codon) == 3:
            amino_acid = RNA_Codons[codon]
            if amino_acid == "*":  # Stop codon
                break
            protein_seq += amino_acid
    return protein_seq
protein_sequence = rna_to_protein(new_rna_sequence)
print("Protein Sequence: " + "\n\n" + protein_sequence)


#reading the DNA sequence from a file 
file_path = './FASTA/hemoglobin-subunit-beta.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read()

# translating the DNA sequence to RNA sequence by using mapping methods
translation_tb  = dna_sequence.maketrans('ATCG', 'UAGC') #maketrans() method is used to create a translation table that maps each character in the first string ('ATCG') to the corresponding character in the second string ('UAGC'). This allows us to easily translate the DNA sequence into an RNA sequence by replacing 'A' with 'U', 'T' with 'A', 'C' with 'G', and 'G' with 'C'.
rna_sequence = dna_sequence.translate(translation_tb) #translate() method is used to perform the actual translation of the DNA sequence into an RNA sequence using the translation table created by maketrans(). It replaces each character in the DNA sequence according to the mapping defined in the translation table, resulting in the corresponding RNA sequence.
print(rna_sequence)

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

protein_sequence = ""
for i in range(0, len(new_rna_sequence), 3):
    codon = new_rna_sequence[i:i+3]
    protein_sequence += RNA_Codons[codon]
print(protein_sequence)
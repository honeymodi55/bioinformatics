from Bio.Seq import Seq


file_path = './FASTA/hemoglobin-subunit-beta.txt'
with open(file_path, 'r') as file:
    dna_sequence = file.read()

dna_seq = Seq(dna_sequence)
rna_seq = dna_seq.transcribe()
print("The transcribed RNA Sequence is: " + "\n\n" + str(rna_seq))

rna_sequence = rna_seq.replace("\n", "").replace(" ", "").strip()

#if you dont want to stop at stop codon (*)
protein_seq = rna_sequence.translate()
print("The translated Protein Sequence is: " + "\n")
print(protein_seq + "\n")

#if you want to stop at stop codon (*)
protein_seq_stop = rna_sequence.translate(to_stop=True)
print("The translated Protein Sequence (stopping at stop codon) is: " + "\n")
print(protein_seq_stop)
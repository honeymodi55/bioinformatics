file_path = "./FASTA/hemoglobin-subunit-beta.txt"
with open(file_path, 'r') as file:
    dna_sequence = file.read()

def calculate_gc_content(dna_seq):
    dna_seq = dna_seq.replace("\n", "").replace(" ", "").strip()  # Remove newlines and spaces
    count_g = dna_seq.count('G')
    count_c = dna_seq.count('C')
    total_gc_content = count_g + count_c
    gc_content_percentage = (total_gc_content/len(dna_seq)) * 100
    return round(gc_content_percentage, 2)

print(f"The GC content percentage is: {calculate_gc_content(dna_sequence)}%")
def transcription(dna_sequence):
    # Replace Thymine (T) with Uracil (U)
    mrna_sequence = dna_sequence.replace('T', 'U')
    
    # Create the Base Pair Complement
    complement = {'A': 'U', 'U': 'A', 'C': 'G', 'G': 'C'}
    complemented_sequence = ''.join([complement[nucleotide] for nucleotide in mrna_sequence])
    
    print("DNA sequence: " + dna_sequence)
    print("mRNA sequence: " + mrna_sequence)
    print("Complement sequence: " + complemented_sequence)
    
    return complemented_sequence

def translation(mrna_sequence):
    # Define a dictionary for codon to amino acid mapping
    codon_table = {
        'UUU': 'Phe', 'UUC': 'Phe',
        'UUA': 'Leu', 'UUG': 'Leu',
        'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
        'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
        'AUG': 'Met',
        'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
        'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
        'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
        'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
        'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
        'UAU': 'Tyr', 'UAC': 'Tyr',
        'UAA': 'Stop', 'UAG': 'Stop',
        'CAU': 'His', 'CAC': 'His',
        'CAA': 'Gln', 'CAG': 'Gln',
        'AAU': 'Asn', 'AAC': 'Asn',
        'AAA': 'Lys', 'AAG': 'Lys',
        'GAU': 'Asp', 'GAC': 'Asp',
        'GAA': 'Glu', 'GAG': 'Glu',
        'UGU': 'Cys', 'UGC': 'Cys',
        'UGA': 'Stop', 'UGG': 'Trp',
        'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',
        'AGU': 'Ser', 'AGC': 'Ser',
        'AGA': 'Arg', 'AGG': 'Arg',
        'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly'
    }
    
    protein_sequence = ""
    i = 0
    
    while i < len(mrna_sequence):
        codon = mrna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, 'X')
        
        # If a stop codon is encountered, terminate translation
        if amino_acid == 'Stop':
            break
        
        protein_sequence += amino_acid
        i += 3

    print("mRNA sequence: " + mrna_sequence)
    print("Protein sequence: " + protein_sequence)
    
    return protein_sequence

# Example usage
dna_sequence = "ATGCTGTAAGTACGTACGTA"
mrna_sequence = transcription(dna_sequence)
protein_sequence = translation(mrna_sequence)

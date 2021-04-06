dna = input('Enter DNA strand: ').upper()

def DNA_strand(dna):
    return dna.translate(str.maketrans("ATCG","TAGC"))

print(DNA_strand(dna))
dna = input('Enter DNA stand: ').upper()

def DNA_strand(dna):
    complement = ""
    ef = []
    
    for x in dna:
        ef.append(x)
    
    for a in range(len(ef)):
        if ef[a] == "A":
            ef[a] = "T"
        elif ef[a] == "T":
            ef[a] = "A"
        elif ef[a] == "G":
            ef[a] = "C"
        elif ef[a] == "C":
            ef[a] = "G"
    
    for y in ef:
        complement += y
        
    return complement

    
print(DNA_strand(dna))
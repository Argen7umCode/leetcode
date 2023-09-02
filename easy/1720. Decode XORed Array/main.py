
def decode(encoded, first):
    decoded = [first]

    for enc in encoded:
        decoded.append(enc ^ decoded[-1])
    
    return decoded

# def decode(encoded, first):
#     decoded = []
#     for 

print(decode([6,2,7,3], 4))
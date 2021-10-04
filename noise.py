import hashlib


def HashValueHex(input):
    h = hashlib.sha256()
    
    try :
        input = bytes(input, "utf8")
    except : 
        print("Cannot parse input to bytes!")
        return None
    
    h.update(input)
    return h.hexdigest()




# Convert sha-256 hash to normalised noise value - profile defines normalisation
def HashToNoise(hash, profile=None, modulus=1000):

    intValue = int(hash, base=16)

    if(intValue > 2^256 - modulus):
        intValue = intValue - modulus
    
    modValue = intValue % modulus
    
    return modValue
    #print("Hash value = " + str(hash))
    #print("Modulus = " + str(modValue))
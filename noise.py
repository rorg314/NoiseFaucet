import hashlib


# Get hash value from input string
def HashValueHex(input):
    # sha256 hasher
    h = hashlib.sha256()
    
    # Convert input to bytes
    try :
        input = bytes(input, "utf8")
    except : 
        print("Cannot parse input to bytes!")
        return None
    # Add to hash
    h.update(input)

    # Return hash value as hex
    return h.hexdigest()


# Convert sha-256 hash to noise value using modular arithmetic (noise value in range 1-modulus)
def HashToNoiseModulus(hash, profile=None, modulus=1000):

    intValue = int(hash, base=16)

    if(intValue > 2^256 - modulus):
        intValue = intValue - modulus
    
    modValue = intValue % modulus
    
    return modValue


# Normalise modular hash value by dividing by modulus
def HashToNoiseNormalised(hash, profile=None, modulus=1000):
    return HashToNoiseModulus(hash, profile=profile, modulus=modulus) / modulus
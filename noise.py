import hashlib
import string
import random


# ======================================================== #
# ================= GENERATE NOISE VALUES ================ #
# ======================================================== #


# Generate random string with specified number of letters
def RandomString(letters=10):
    chars = string.ascii_letters
    return  ''.join(random.choice(chars) for i in range(letters)) 


# Get hash value from input string
def StringToHexHash(input):
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


# Convert sha-256 hash to noise value using modular arithmetic (noise value in range [1, modulus])
def HashToNoiseModulus(hash, modulus=1000):

    intValue = int(hash, base=16)

    if(intValue > 2^256 - modulus):
        intValue = intValue - modulus
    
    modValue = intValue % modulus
    
    return modValue


# Normalise modular hash value by dividing by modulus
def HashToNoiseNormalised(hash, modulus=1000):
    return HashToNoiseModulus(hash, modulus=modulus) / modulus



# ======================================================== #
# ====================== ITERATIONS ====================== #
# ======================================================== #



# Return an average noise value over 'iters' iterations
# Uses letters=N to generate random string with N upper/lowercase characters - hash of this string is used to generate noise value 
def NoiseValueIterations(iters=1, letters=10, modulus=1000):

    noiseValues = list()

    for i in range(iters):
        # Generate random string
        randomString = RandomString(letters=letters)
        # Generate hash value
        hash = StringToHexHash(randomString)
        # Generate noise value
        noiseVal = HashToNoiseNormalised(hash, modulus=modulus)
        noiseValues.append(noiseVal)

    return noiseValues


# Returns the average noise value over specified number of iterations
def AverageNoiseValue(iters, letters=10, modulus=1000):
    values = NoiseValueIterations(iters=iters, letters=letters, modulus=modulus)

    return sum(values) / len(values)


# Returns average after re-centering values
def AverageOneCenteredNoiseValue(iters, letters=10, modulus=1000):
    values = NoiseValueIterations(iters=iters, letters=letters, modulus=modulus)

    recenteredValues = RecenterNoiseValues(values, oldCenter=0.5, newCenter=1)

    return sum(recenteredValues) / len(recenteredValues)



# ======================================================== #
# ======================= UTILITIES ====================== #
# ======================================================== #


# Add bias to normalised (0-1) noise values to center all values around 'newCenter' (old center = 0.5) 
def RecenterNoiseValues(noiseValues, oldCenter=0.5, newCenter=1):

    # Calculate bias as newCenter - oldCenter
    bias = newCenter - oldCenter

    # If list, add bias to all values
    if(isinstance(noiseValues, list)):
        return [val + bias for val in noiseValues]
    # If single int or float add bias and return
    elif(isinstance(noiseValues, int) or isinstance(noiseValues, float)):
        return noiseValues + bias
    # If recieved invalid input type
    else:
        print("RecenterNoise recieved invalid input type! " + str(type(noiseValues)))

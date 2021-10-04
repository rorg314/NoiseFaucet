from matplotlib import pyplot as plt
import string
import random
from noise import *

# Test a series of random data generates random hashes
def test_AverageOverIterations(iterations=1e3, modulus=1000):
    i = 0
    allNoiseValues = list()
    while (i < iterations):
        # Generate random string
        data = RandomString()
        # Hash hex value
        hashHex = HashValueHex(data)
        # Convert to modulus noise value
        noiseValue = HashToNoise(hashHex, modulus=modulus) / modulus
        allNoiseValues.append(noiseValue)
        print(i)
        i = i+1
    avg = sum(allNoiseValues)/len(allNoiseValues)
    return avg

    fig, axs = plt.subplots()
    axs.plot(allNoiseValues, 'bo')
    plt.show()
    print("Average noise value = " + str(avg))


def test_AverageOverBatchOfIterations(batches=1e3, iter=1e3, modulus=1000):
    b = 0 
    allBatchAverages = list()
    while (b < batches):
        avg = test_AverageOverIterations(iterations=iter, modulus=modulus)
        allBatchAverages.append(avg)
        b = b+1
    
    print("Min average = " + str(min(allBatchAverages)))
    print("Max average = " + str(max(allBatchAverages)))
    print("Average average = " + str(sum(allBatchAverages)/len(allBatchAverages)))
    
    fig, axs = plt.subplots()
    axs.plot(allBatchAverages, 'bo')
    plt.show()




def RandomString(letters=10):
    chars = string.ascii_letters
    return  ''.join(random.choice(chars) for i in range(letters)) 

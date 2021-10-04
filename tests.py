from matplotlib import pyplot as plt

from noise import *

# Test a series of random data generates random hashes
def test_AverageOverIterations(iterations=1e3, modulus=1000):
    noiseValues = NoiseValueIterations(iterations, modulus=modulus, letters=10)

    avg = sum(noiseValues) / len(noiseValues)

    return avg
    


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






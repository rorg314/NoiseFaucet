from matplotlib import pyplot as plt

from faucet import *
from noise import *

# Test a series of random data generates random hashes
def test_AverageOverIterations(iterations=1e3, modulus=1000):
    noiseValues = NoiseValueIterations(iterations, modulus=modulus, letters=10)

    avg = sum(noiseValues) / len(noiseValues)

    return avg
    

# Test the average over a number of batches (each with 'iter' iterations)
def test_AverageOverBatchOfIterations(batches=1e3, iter=1e3, modulus=1000):
    b = 0 
    allBatchAverages = list()
    while (b < batches):
        avg = test_AverageOverIterations(iterations=int(iter), modulus=modulus)
        allBatchAverages.append(avg)
        b = b+1
    
    print("Min average = " + str(min(allBatchAverages)))
    print("Max average = " + str(max(allBatchAverages)))
    print("Average average = " + str(sum(allBatchAverages)/len(allBatchAverages)))
    
    fig, axs = plt.subplots()
    axs.plot(allBatchAverages, 'bo')
    plt.show()


# Test net diff after a number of transactions
def test_NetDiffAfterNumTransactions(num=1e1):
    faucet = Faucet()
    testUser = User('Test', faucet, userBalance=BtcToSat(1))

    iters = 1000

    allDiffs = list()

    i=0
    while i < num:
        transaction = UserMakeTransaction(testUser, BtcToSat(0.001), iters)
        allDiffs.append(transaction.diff)
        testUser.userBalance = BtcToSat(1)
        i=i+1
    
    fig, axs = plt.subplots()
    axs.plot(allDiffs, 'bo')
    axs.set_xlabel("Site balance = " + BtcStr(SatToBtc(faucet.siteBalance)))
    plt.show()

    return sum(allDiffs)

    

def test_NetDiffAfterBatches(batches=1e3, num=1e1):
    faucet = Faucet()
    testUser = User('Test', faucet, userBalance=BtcToSat(1))
    iters = 1000

    allBatchDiffs = list()

    b = 0
    while b < batches:
        i = 0
        while i < num:
            transaction = UserMakeTransaction(testUser, BtcToSat(0.001), iters)
            allBatchDiffs.append(transaction.diff)
            testUser.userBalance = BtcToSat(1)
            i=i+1
        
        transaction = UserMakeTransaction(testUser, BtcToSat(0.001), iters)
        
        i = i+1

    fig, axs = plt.subplots()
    axs.plot(allBatchDiffs, 'bo')
    axs.set_xlabel("Site balance = " + BtcStr(SatToBtc(faucet.siteBalance)))
    plt.show()


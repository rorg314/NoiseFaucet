from matplotlib import pyplot as plt

from faucet import *
from noise import *

# Test a series of random data generates random hashes
def test_AverageOverIterations(iterations=1e3, modulus=1000):
    noiseValues = NoiseValueIterations(int(iterations), modulus=modulus, letters=10)

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
    testUser = User('Test', faucet, userSiteBalance=BtcToSat(1))

    iters = 1000

    allDiffs = list()

    i=0
    while i < num:
        transaction = UserMakeTransaction(testUser, BtcToSat(0.001), iters)
        allDiffs.append(transaction.diff)
        testUser.userSiteBalance = BtcToSat(1)
        i=i+1
    
    fig, axs = plt.subplots()
    axs.plot(allDiffs, 'bo')
    axs.set_xlabel("Site balance = " + BtcStr(SatToBtc(faucet.siteBalance)))
    plt.show()

    return sum(allDiffs)


# Test average diff per batch
def test_NetDiffAfterBatches(batches=1e2, num=1e2):
    faucet = Faucet()
    testUser = User('Test', faucet, userSiteBalance=BtcToSat(1))
    iters = 1000

    allBatchDiffs = list()

    b = 0
    while b < batches:
        i = 0
        batchDiffs = list()
        while i < num:
            transaction = UserMakeTransaction(testUser, BtcToSat(0.001), iters)
            batchDiffs.append(transaction.diff)
            testUser.userSiteBalance = BtcToSat(1)
            i=i+1
        allBatchDiffs.append(sum(batchDiffs)/len(batchDiffs))
        b = b+1

    fig, axs = plt.subplots()
    axs.plot(allBatchDiffs, 'bo')
    axs.set_xlabel("Site balance = " + BtcStr(SatToBtc(faucet.siteBalance)))
    plt.show()


# Test number of transactions before bankrupt
def test_NumUserTransactions(amount=BtcToSat(0.01), num=1e5):
    faucet = Faucet()
    # Start with 1 BTC
    testUser = User('Test', faucet, userSiteBalance=BtcToSat(1))
    iters = 1000
    
    userSiteBalances = list()
    userSiteBalances.append(testUser.userSiteBalance)
    startBal = testUser.userSiteBalance
    # Transfer constant amount 
    #while testUser.userSiteBalance > 0:
    for i in range(int(num)):
        if(testUser.userSiteBalance <= 0.5 * startBal):
            print("Bankrupt")
            break
        transaction = UserMakeTransaction(testUser, amount, iters)

        userSiteBalances.append(testUser.userSiteBalance)
        
    fig, axs = plt.subplots()
    axs.plot(userSiteBalances)
    axs.set_title("Total transactions: " + str(len(userSiteBalances)) +"\nSiteBal = " + BtcStr(SatToBtc(faucet.siteBalance)) )
    plt.show()
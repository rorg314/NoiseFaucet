
from faucet import *



def main():
    print("main")
    
    faucet = Faucet()
    testUser = User('Test', faucet, userBalance=BtcToSat(1))

    iters = 1000

    UserMakeTransaction(testUser, BtcToSat(0.001), iters)








if __name__ == '__main__':
    main()



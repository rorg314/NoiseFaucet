from collections import defaultdict
import datetime
from random import random



from noise import AverageNoiseValue, AverageOneCenteredNoiseValue
from util import BtcStr, BtcToSat, SatToBtc


class Faucet():
    def __init__(self):
        # Money the site owns
        self.siteBalance = 0
        # Coins held in escrow on the site
        self.escrowBalance = 0
        # List of all users
        self.allUsers = list()
        # List of all transactions
        self.allTransactions = list()
        

class User():
    def __init__(self, name:str, faucet:Faucet, userSiteBalance=0):
        # Add user to site
        self.site = faucet
        faucet.allUsers.append(self)
        # Username
        self.name = name

        # Balance the user has (NOT on site)
        self.userBalance = 0
        # Coins the user has on the site
        self.userSiteBalance = userSiteBalance
        # List of all user transactions
        self.allTransactions = list()
    
    def __repr__(self) -> str:
        return self.name


class Transaction():
    def __init__(self, user:User, amount:int, iters=100):
        # User that initiated the transaction
        self.user = user
        # Store transaction time
        self.time = datetime.time()
        # Add transaction to site
        self.user.site.allTransactions.append(self)
        # Add transaction to user
        self.user.allTransactions.append(self)

        # Amount the user sent
        self.amount = amount

        # Calculated noise value (normalised between -0.5 to 0.5 )
        self.avgNoiseValue = AverageOneCenteredNoiseValue(iters, letters=10, modulus=1000)

        # Noise multiplied value of this transaction 
        self.noiseMultipliedValue = self.amount * self.avgNoiseValue

        # Overall difference, positive returned to user negative to site
        self.diff = self.noiseMultipliedValue - self.amount


# ======================================================== #
# ===================== TRANSACTIONS ===================== #
# ======================================================== #


# Returns true if user has enough to send transaction
def ValidTransaction(user:User, amount:int):
    return user.userSiteBalance > amount


# User sends btc to site (amounts must be in sats)
def UserMakeTransaction(user:User, amount:int, iters:int):
    
    # Check if valid transaction
    if(not ValidTransaction(user, amount)):
        print("User balance was too low! User: " + user.name)
        return
    
    # Remove amount from user balance
    user.userSiteBalance -= amount

    # Create the transaction object
    transaction = Transaction(user, amount, iters=iters)

    # Return the amount to the user
    user.userSiteBalance += amount

    # Add/subtract diff from user site balance
    user.userSiteBalance += transaction.diff
    user.site.siteBalance -= transaction.diff
    
    return transaction

    #print("User " + str(user.name) + " : sent=" + BtcStr(SatToBtc(amount)) + " : noise=" + f"{transaction.avgNoiseValue:1.5f}" + " : diff=" + BtcStr(SatToBtc(transaction.diff)))




# ======================================================== #
# ====================== TEST USERS ====================== #
# ======================================================== #


# Create a user with a random balance (as a random % of 1BTC)
def CreateRandomUser(faucet:Faucet, name=""):

    startBal = BtcToSat( random.range(1, 100) / 100 )

    usr = User(name, faucet, userBalance=startBal)


# Create a specified number of random users
def CreateNumRandomUsers(faucet:Faucet, number):

    for i in range(number):
        CreateRandomUser(faucet, name=str(i))


def CreateTestFacuet(users=1):
    
    faucet = Faucet()
    #CreateNumRandomUsers(faucet, users)
    testUser = User('Test', faucet, userBalance=BtcToSat(1))

    return faucet, testUser


# ======================================================== #
# ========================= STATS ======================== #
# ======================================================== #


def PlotAllTransactionReturns(site:Faucet):
    print(2)

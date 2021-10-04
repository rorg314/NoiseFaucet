from collections import defaultdict
import datetime
from random import random



from noise import AverageNoiseValue, AverageZeroCenteredNoiseValue
from util import BtcToSat


class Site():
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
    def __init__(self, name:str, site:Site, userBalance=0):
        # Add user to site
        self.site = site
        site.allUsers.append(self)
        # Username
        self.name = name

        # Balance the user has (NOT on site)
        self.userBalance = userBalance
        # Coins the user has on the site
        self.userSiteBalance = 0
        # List of all user transactions
        self.allTransactions = list()


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
        self.avgNoiseValue = AverageZeroCenteredNoiseValue(iters, letters=10, modulus=1000)

        # Noise multiplied value of this transaction 
        self.noiseMultipliedValue = self.amount * self.avgNoiseValue

        # Overall difference, positive returned to user negative to site
        self.diff = self.noiseMultipliedValue - self.amount


# ======================================================== #
# ===================== TRANSACTIONS ===================== #
# ======================================================== #


# Returns true if user has enough to send transaction
def ValidTransaction(user:User, amount:int):
    return user.userBalance > amount


# User sends btc to site (amounts must be in sats)
def UserMakeTransaction(user:User, amount:int, iters:int, txFee=1000):
    
    # Check if valid transaction
    if(not ValidTransaction(user, amount)):
        print("User balance was too low! User: " + user.name)
        return
    
    # Remove amount from user balance
    user.userBalance -= amount

    # Send to user site balance (- txFee)
    user.userSiteBalance += amount - txFee

    # Create the transaction object
    transaction = Transaction(user, amount, iters=iters)

    # Add/subtract diff from user site balance
    if(transaction.diff > 0):
        user.userSiteBalance += transaction.diff
    elif(transaction.diff <= 0):
        user.userSiteBalance -= transaction.diff
        user.site.siteBalance += transaction.diff



# ======================================================== #
# ====================== TEST USERS ====================== #
# ======================================================== #


# Create a user with a random balance (as a random % of 1BTC)
def CreateRandomUser(site:Site, name=""):

    startBal = BtcToSat( 1 / random.range(100) )

    usr = User(name, site, userBalance=startBal)


# Create a specified number of random users
def CreateNumRandomUsers(site:Site, number):

    for i in range(number):
        CreateRandomUser(site, name=str(i))




# ======================================================== #
# ========================= STATS ======================== #
# ======================================================== #


def PlotAllTransactionReturns(site:Site):
    print(2)

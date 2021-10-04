from collections import defaultdict
import datetime
from noise import AverageNoiseValue, AverageRecenteredNoiseValue



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
    def __init__(self, site:Site, user:User, amount:int, iters=100):
        # Ref to the site
        self.site = site
        # Store transaction time
        self.time = datetime.time()
        
        
        # User that initiated the transaction
        self.user = user
        # Amount the user sent
        self.amount = amount

        # Calculated noise value (normalised between 0.5 - 1.5 )
        self.avgNoiseValue = AverageRecenteredNoiseValue(iters, letters=10, modulus=1000)

def ValidTransaction(user:User, amount:int):
    return user.userBalance > amount


# User sends btc to site (amounts must be in sats)
def UserMakeTransaction(user:User, amount:int):
    # Check if valid transaction
    if(not ValidTransaction(user, amount)):
        print("User balance was too low! User: " + user.name)
        return
    
    # Remove amount from user balance
    user.userBalance -= amount
    # Send to user site balance
    user.userSiteBalance += amount






from collections import defaultdict



class Site():
    def __init__(self):
        # Money the site owns
        self.siteBalance = 0
        # Coins held in escrow on the site
        self.escrowBalance = 0
        # Dict of user -> coins held on site
        self.userSiteBalanceDict = dict()
        # Dict with user -> list of all user transactions
        self.userTransactionsDict = defaultdict(list)


class User():
    def __init__(self, userBalance=0):
        # Balance the user has (NOT on site)
        self.userBalance = userBalance

        # Coins the user has on the site
        self.userSiteBalance = 0
        # List of all user transactions
        self.allTransactions = list()



class Transaction():
    def __init__(self, site:Site, user:User, amount:int, iters=1):
        # Ref to the site
        self.site = site
        # User that initiated the transaction
        self.user = user

        # Amount the user sent
        self.amount = amount

        # Calculated noise value (normalised between 0.5 - 1.5 )
        self.noiseValue = 0






# User sends coins to the site
def SendCoins(amount:int)
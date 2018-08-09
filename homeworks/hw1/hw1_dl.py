import random
import datetime
now = datetime.datetime.now()

## Create Stock with price and name
class Stocks(object):
  def __init__(self, price, name):
      self.price = float(price)
      self.name = name
  def __str__(self):
      return '%.f, %s' % (self.price, self.name)

 ## Create MutualFund with symbol
class MutualFund(object):
 def __init__(self,name):
     self.name = name
 def __str__(self):
      return '%s' % (self.name)


class Portfolio(object):
    def __init__(self):
        self.cash = 0
        self.hist= [('Account created: %d-%d-%d %d:%d - $ 0' % (now.year, now.month, now.day, now.hour, now.minute))]
        #port = {"Stock" : {}, "Mutual_Fund" : {}}

    ## Add cash to the portfolio
    def addCash(self,amount):
        self.cash += float(amount)
        self.hist.append('Deposited $%.f: %d-%d-%d %d:%d - $ %.2f' % (amount, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
        return self.cash
    
    ## Buys stock with the number of shares and the particular stock 
    def buyStock(self,shares, stock):
        if float(shares * stock.price) > self.cash:
            print "Transaction error: Insufficient funds"
        else:
            self.cash -= (shares*stock.price)
            self.hist.append ('Purchased %.2f of %s: %d-%d-%d %d:%d - $ %.2f' % (shares, stock, now.year, now.month, now.day, now.hour, now.minute,self.cash) )
        return self.cash
    

    ## Buy mutual funds (1$ a piece)
    def buyMutualFunds(self, shares):
        if float(shares ) > self.cash:
            print "Transaction error: Insufficient funds"
        self.cash -= float(shares)
        hist.append = ('Purchased %.2f of %s: %d-%d-%d %d:%d - $ %.2f' % (now.year, now.month, now.day, now.hour, now.minute, self.cash) )

   
    ## Print the portfolio
    def __str__(self):
        print "cash: %.2f" % self.cash
        print 
        print 
        

    ##  Sell mutual fund with number of shares
    def sellMutualFund(self, shares):
        hist.append = ('Sold $%.f of Mutual Funds : %d-%d-%d %d:%d - $%.2f' % (shares, now.year, now.month, now.day, now.hour, now.minute, self.cash) )




    ## Sell stock by number of shares and stock name
    def sellStock(self, shares, stock):
        hist.append = ('Sold $%.f of %s: %d-%d-%d %d:%d -$%.2f' % (price, stock, now.year, now.month, now.day, now.hour, now.minute, self.cash) )



    ## Withraw cash
    def withdraw(self, amount):
        hist.append = ('Account created: %d-%d-%d %d:%d - $ %.2f' % (now.year, now.month, now.day, now.hour, now.minute) )




  



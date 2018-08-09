import random
import datetime
now = datetime.datetime.now()

## Create Stock with price and name
class Stocks(object):
  def __init__(self, price, name):
      self.price = price
      self.name = name

 ## Create MutualFund with symbol
class MutualFund(object):
 def __init__(self,name):
     self.stock_type = stock_type
     self.stock_price = stock_price


class Portfolio(object):
    def __init__(self):
        self.cash = cash
        self.stock = stock
        self.mfund = mutual_fund
        self.trans = ('Account created: %d-%d-%d %d:%d - $ 0' % (now.year, now.month, now.day, now.hour, now.minute) )
       

    ## Add cash to the portfolio
    def addCash(self,amount):
        self.cash += float(amount)
        self.trans.append = ('Deposited $%.f: %d-%d-%d %d:%d ' % (now.year, now.month, now.day, now.hour, now.minute, self.cash) )
        return self.cash
    
    ## Buys stock with the number of shares and the particular stock 
    def buyStock(self,shares, stock):
        self.cash -= float(amount)
        self.trans.append = ('Account created: %d-%d-%d %d:%d ' % (now.year, now.month, now.day, now.hour, now.minute,self.cash) )

        
    

    ## Buy mutual funds (1$ a piece)
    def __eq__(self, shares):
        self.cash -= float(shares)
        self.trans.append = ('Account created: %d-%d-%d %d:%d ' % (now.year, now.month, now.day, now.hour, now.minute, self.cash) )

   
    ## Print the portfolio
    def __str__(self):
        print self.cash
        print 
        

    ##  Sell mutual fund with number of shares
    def sellMutualFund(self, shares):
        self.trans.append = ('Sold $%.f of Mutual Funds : %d-%d-%d %d:%d - %f' % (shares, now.year, now.month, now.day, now.hour, now.minute, self.cash) )




    ## Sell stock by number of shares and stock name
    def sellStock(self, shares, stock):
        self.trans.append = ('Sold $%.f of %s: %d-%d-%d %d:%d -%f' % (price, stock, now.year, now.month, now.day, now.hour, now.minute, self.cash) )



    ## Withraw cash
    def withdraw(self, amount):
        self.trans = ('Account created: %d-%d-%d %d:%d ' % (now.year, now.month, now.day, now.hour, now.minute) )




  



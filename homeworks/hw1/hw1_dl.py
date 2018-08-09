import random
import datetime
now = datetime.datetime.now()

## Create Stock with price and name
class Stocks(object):
  def __init__(self, price, name): #initialize the stock type
      self.price = float(price)
      self.name = name
  def __str__(self):
      return '%.f, %s' % (self.price, self.name)

 ## Create MutualFund with symbol
class MutualFund(object): #initialize the mf type
 def __init__(self,name):
     self.name = name
 def __str__(self):
      return '%s' % (self.name)


class Portfolio(object): #initialize cash 
    def __init__(self):
        self.cash = 0 #this is an object (?) which will store the running balance
        self.port = {"Stock" : [], "Mutual_Fund" : []} #a place to store the stocks and mutual funds in order to print them
        self.hist= [('Account created: %d-%d-%d %d:%d - $0' % (now.year, now.month, now.day, now.hour, now.minute) )]#transaction history
        self.stock= []
        self.mf= []

    ## Add cash to the portfolio
    def addCash(self,amount):
        self.cash += float(amount)
        self.hist.append('Deposited $%.f: %d-%d-%d %d:%d - $%.2f' % (amount, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
        return self.cash
    
    ## Buys stock with the number of shares and the particular stock 
    def buyStock(self,shares, stock):
        if float(shares * stock.price) > self.cash:
            print "Transaction error: Insufficient funds"
        else:
            self.cash -= (shares*stock.price)
            self.hist.append('Purchased %.2f of %s: %d-%d-%d %d:%d - $%.2f' % (shares, stock.name, now.year, now.month, now.day, now.hour, now.minute,self.cash))
            if len(self.stock) == 0:
                self.stock.append([stock.price, stock.name])
            else:
                #if stock.name in self.stock:
                #    self.stock[stock.name] += shares
                #    else: 
                self.stock.append([stock.price, stock.name])
        return self.cash
    

    ## Buy mutual funds (1$ a piece)
    def buyMutualFunds(self, shares, mf):
        if float(shares ) > self.cash:
            print "Transaction error: Insufficient funds"
        else:
            self.cash -= float(shares)
            self.hist.append ('Purchased %.2f of %s: %d-%d-%d %d:%d - $%.2f' % (shares, mf.name, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
            if len(self.mf) == 0:
                self.mf.append([shares, mf.name])
            else:
                #for i in self.mf:
                #    if i[1] == mf.name:
                #        temp = i[0] + shares
                #        i[0] = temp
                #    else: 
                self.mf.append([shares, mf.name])
        return self.cash

   
    ## Print the portfolio
    def __str__(self):
        print "cash: %.2f" % self.cash
        p = {"Stock": (self.stock), "Mutual_Fund": (self.mf)}
        print p       

    ##  Sell mutual fund with number of shares
    def sellMutualFund(self, shares):
        self.cash += (shares * random.uniform(.9,1.2))
        self.hist.append = ('Sold $%.f of Mutual Funds : %d-%d-%d %d:%d - $%.2f' % (shares, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
        

    ## Sell stock by number of shares and stock name
    def sellStock(self, shares, stock):
        self.cash += (shares * random.uniform((.5*stock.price),(1.2*stock.price))
        self.hist.append('Sold $%.f of %s: %d-%d-%d %d:%d -$%.2f' % (price, stock, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
        if stock.name in self.stock:
            self.stock[stock.name] -= shares
        return self.cash

    ## Withraw cash
    def withdraw(self, amount):
        self.hist.append = ('Withdrew %.2f from account: %d-%d-%d %d:%d - $ %.2f' % (amount,now.year, now.month, now.day, now.hour, now.minute) )

    def history(self):
        print  '\n'.join(me.hist)




  



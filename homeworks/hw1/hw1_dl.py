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
        self.port = {"Stock" :{}, "Mutual_Fund" :{}} #a place to store the stocks and mutual funds in order to print them
        self.hist= [('Account created: %d-%d-%d %d:%d - $0' % (now.year, now.month, now.day, now.hour, now.minute) )]#transaction history
       
    ## Add cash to the portfolio
    def addCash(self,amount):
        self.cash += float(amount)
        self.hist.append('Deposited $%.f: %d-%d-%d %d:%d - $%.2f' % (amount, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
        return self.cash
    
    ## Buys stock with the number of shares and the particular stock 
    def buyStock(self,shares, stock):
        if shares %1 != 0:
            print "Share number must be whole number"
        else:
            if float(shares * stock.price) > self.cash:
                print "Transaction error: Insufficient funds"
                self.hist.append("Failed attempt to purchase stocks")

            else:
                self.cash -= (shares*stock.price)
                self.hist.append('Purchased %.2f of %s: %d-%d-%d %d:%d - $%.2f' % (shares, stock.name, now.year, now.month, now.day, now.hour, now.minute,self.cash))
                if stock.name in self.port["Stock"]: ## Yikes, had to get help here
                    self.port["Stock"][stock.name]+=shares ## Worked on a for loop for HOURS but gave up got guidance
                else:
                    self.port["Stock"].update({stock.name:shares})
        return self.cash
    

    ## Buy mutual funds (1$ a piece)
    def buyMutualFunds(self, shares, mf):
        if shares %1 != 0:
            print "Share number must be whole number"
        else:
            if float(shares ) > self.cash:
                print "Transaction error: Insufficient funds"
                self.hist.append("Failed attempt to purchase mutual funds")
            else:
                 self.cash -= float(shares)
                 self.hist.append ('Purchased %.2f of %s: %d-%d-%d %d:%d - $%.2f' % (shares, mf.name, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
                 if mf.name in self.port["Mutual_Fund"]:
                     self.port["Mutual_Fund"][mf.name]-=shares
                 else:
                     self.port["Mutual_Fund"].update({mf.name:shares})
        return self.cash

   
    ## Print the portfolio
    def __str__(self):
        print "cash: %.2f" % self.cash
        return str(me.port )    

    ##  Sell mutual fund with number of shares
    def sellMutualFund(self, shares, mf):
          if shares %1 != 0:
            print "Share number must be whole number"
          else:
              self.cash += (shares * random.uniform(.9,1.2))
              self.hist.append = ('Sold $%.f of Mutual Funds : %d-%d-%d %d:%d - $%.2f' % (shares, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
              if stock.name in self.port["Mutual_Fund"]: ## Yikes, had to get help here
                    self.port["Mutual_Fund"][mf.name]+=shares ## Worked on a for loop for HOURS but gave up got guidance
              else:
                    self.port["Mutual_Fund"].update({mf.name:shares})
              return self.cash

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



a=Stocks(1,"a")
b=Stocks(2,"b")
c=MutualFund("c")
d=MutualFund("d")
e=MutualFund("e")
me=Portfolio()
me.addCash(22)
me.buyStock(3,a)
me.buyStock(1,b)
me.buyStock(1.2,b)# Here we see an error if not using whole numbers
me.buyMutualFunds(5,c)
me.buyMutualFunds(20,d) # Here we see the error from not enough money

me.buyMutualFunds(1,d)# BEHOLD:
me.buyMutualFunds(1,d)# these fuckers combine in our dictionary
print me
me.sellMutualFund(2,a)

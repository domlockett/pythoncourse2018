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
    
    ## Buys stock with the number of shares and the particular stock 
    def buyStock(self,shares, stock):
        if shares %1 != 0:
            print "Transaction error: Share number must be whole number"
            self.hist.append("Failed attempt to purchase stocks - $%.2f" %  self.cash)

        else:
            if float(shares * stock.price) > self.cash:
                print "Transaction error: Insufficient funds"
                self.hist.append("Failed attempt to purchase stocks - $%.2f" %  self.cash)

            else:
                self.cash -= (shares*stock.price)
                self.hist.append('Purchased %.2f of %s: %d-%d-%d %d:%d - $%.2f' % (shares, stock.name, now.year, now.month, now.day, now.hour, now.minute,self.cash))
                if stock.name in self.port["Stock"]: ## Yikes, had to get help here
                    self.port["Stock"][stock.name]+=shares ## Worked on a for loop for HOURS but gave up got guidance
                else:
                    self.port["Stock"].update({stock.name:shares})
    

    ## Buy mutual funds (1$ a piece)
    def buyMutualFunds(self, shares, mf):
        if shares %1 == 0:
            print "Transaction error: Share number must be fraction"
            self.hist.append("Failed attempt to purchase mutual fund - $%.2f" %  self.cash)

        else:
            if float(shares ) > self.cash:
                print "Transaction error: Insufficient funds"
                self.hist.append("Failed attempt to purchase mutual funds - $%.2f" %  self.cash)
            else:
                 self.cash -= float(shares)
                 self.hist.append ('Purchased %.2f of %s: %d-%d-%d %d:%d - $%.2f' % (shares, mf.name, now.year, now.month, now.day, now.hour, now.minute, self.cash) )
                 if mf.name in self.port["Mutual_Fund"]:
                     self.port["Mutual_Fund"][mf.name]+=shares
                 else:
                     self.port["Mutual_Fund"].update({mf.name:shares})

   
    ## Print the portfolio
    def __str__(self):
        print "cash: %.2f" % self.cash
        return str(self.port )    

    ##  Sell mutual fund with number of shares
    def sellMutualFund(self, shares, mf):
        if shares %1 == 0:
            print "Transaction Error: Share number must be fraction"
            self.hist.append("Failed attempt to sell mutual funds - $%.2f" %  self.cash)

        else:
            if shares > self.port["Mutual_Fund"][mf.name]:
                print "Transaction error:Cannot sell more shares than you own"
                self.hist.append("Failed attempt to sell mutual funds - $%.2f" %  self.cash)

            else:
                self.cash += (shares * random.uniform(.9,1.2))
                self.hist.append('Sold $%.f of %s : %d-%d-%d %d:%d - $%.2f' % (shares,mf.name, now.year, now.month, now.day, now.hour, now.minute, self.cash))
                if mf.name in self.port["Mutual_Fund"]:
                    self.port["Mutual_Fund"][mf.name]-=shares 
                else:
                   self.port["Mutual_Fund"].update({mf.name:shares})

    ## Sell stock by number of shares and stock name
    def sellStock(self, shares, stock):
        if shares %1 != 0:
           print "Transaction error: Share number must be whole number"
           self.hist.append("Failed attempt to sell stocks - $%.2f" %  self.cash)

        else:
            if shares > self.port["Stock"][stock.name]:
                print "Cannot sell more shares than you own"
                self.hist.append("Failed attempt to sell stocks - $%.2f" %  self.cash)

            else:
                self.cash += (shares * random.uniform((.5*stock.price),(1.2*stock.price)))
                self.hist.append('Sold $%.f of %s : %d-%d-%d %d:%d - $%.2f' % (shares,stock.name, now.year, now.month, now.day, now.hour, now.minute, self.cash))
                if stock.name in self.port["Stock"]:
                    self.port["Stock"][stock.name]-=shares
                else:
                    self.port["Stock"].update({stock.name:shares})

    ## Withraw cash
    def withdraw(self, amount):
        if amount > self.cash:
            print "Transaction error: Insufficient Funds"
            self.hist.append("Failed attempt to withdraw cash - $%.2f" %  self.cash)

        else:
            self.cash -= float(amount)
            self.hist.append('Withdrew %.2f from account: %d-%d-%d %d:%d - $ %.2f' % (amount,now.year, now.month, now.day, now.hour, now.minute, self.cash))
    ## history of transactions
    def history(self):
        print "Transaction history:"
        print  '\n'.join(self.hist)



a=Stocks(1,"a") #make some stocks
b=Stocks(2,"b")
c=MutualFund("c") #make some mutual funds
d=MutualFund("d")
e=MutualFund("e")
me=Portfolio()
me.addCash(220) #add cash

me.buyStock(3,a) #add stock 
me.buyStock(1,b)
me.buyStock(1.2,b)# Here we see an error if not using whole numbers

me.buyMutualFunds(.5,c)#add mutual fund
me.buyMutualFunds(12.5,c)
me.buyMutualFunds(400.1,d) # Here we see the error from not enough money

me.buyMutualFunds(.91,d)# BEHOLD:
me.buyMutualFunds(.9,d)# these fuckers combine in our dictionary
print me #print portfolio

me.sellMutualFund(1.81,d)# sell stock
print me
me.buyStock(2,a)
me.sellStock(2,a)
print me
me.sellStock(.5,b) #Can't sell stocks as fractions
me.sellStock(40,b) #cant sell more than you own
me.withdraw(200)
me.withdraw(500)#Cat't withdraw more than you own
me.history()

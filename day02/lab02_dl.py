## Fill in the following methods for the class 'Clock'

class Clock(object):
    def __init__(self, hour, minutes):

       
        self.minutes = minutes
        self.hour = hour

    @classmethod
    def at(cls, hour, minutes=0):
        return cls(hour, minutes)

    ## Print the time
    def __str__(self):
        return "%d:%02d" % (self.hour, self.minutes)
     
    ## Add time
    ## Don't return anythhing
    def __add__(self,minutes):
        if minutes > 1440: print "too many minutes honey"
        else:
            hour = self.hour + int(minutes/60)
            minutes = self.minutes + ((minutes%60))
        return "%d:%02d" % (hour, minutes)
    
    ## Subtract time
    ## Don't return anything
    def __sub__(self,minutes):
        if minutes > 1440: print "too many minutes honey"
        else:
            hour = self.hour - int(minutes/60)
            minutes = self.minutes - ((minutes%60))
        return "%d:%02d" % (hour, minutes)
    ## Are two times equal?
    def __eq__(self, other):
        return (self.hour==other.hour and self.minutes==other.minutes)
    ## Are two times not equal?
    def __ne__(self, other):
        return (self.hour!=other.hour or self.minutes!=other.minutes)

x = Clock(1, 30)
y = Clock(1, 30)

x != y
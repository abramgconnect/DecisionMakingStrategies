import random

class KarmedBandits():
    def Button1(self):
        return 12
        #expected reward=12*1=12
    def Button2(self):
        return random.uniform(16,25)
        #expected reward= 16+((25-16)/2)=20.5

    def Button3(self):
        var=random.randint(1,100)
        if var<=94:
            return 12
        else:
            return 486
        #expected reward = 0.94*12+0.6*486=40.44

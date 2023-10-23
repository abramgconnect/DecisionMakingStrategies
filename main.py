import math
import random
from GamesLib import KarmedBandits

import numpy as np
import matplotlib.pyplot as plt



def RandomActionSelection(trials):
    Q1 = np.array([])
    Q2 = np.array([])
    Q3 = np.array([])
    Game = KarmedBandits()
    rewards=0
    for i in range(0, trials):
        ChosenButton = random.randint(1, 3)
        if ChosenButton == 1:
            r=Game.Button1()
            Q1 = np.append(Q1, r)
            rewards +=r

        elif ChosenButton == 2:
            r = Game.Button2()
            Q2 = np.append(Q2, r)
            rewards += r
        else:
            r = Game.Button3()
            Q3 = np.append(Q3, r)
            rewards += r
    print('values for the 3 buttons',np.average(Q1), np.average(Q2), np.average(Q3))
    return(rewards)

def RandomActionSelectionIUR(trials):
    #better Memory consumption, just 6 numbers to store
    #Keeping Qx_n fixed for "Non Stationary" Problems as choosing medicine in different seasons
    #Non Stationary Problems mean reward distribution changes with time
    #Use DecayingRewards function to visualize decaying
    #alpha may be called learning rate
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q1_n = 0
    Q2_n = 0
    Q3_n = 0
    Game = KarmedBandits()
    rewards=0
    for i in range(0, trials):
        ChosenButton = random.randint(1, 3)
        if ChosenButton == 1:
            r = Game.Button1()
            Q1_n += 1
            Q1 = Q1+(1/Q1_n)*(r-Q1)
            rewards +=r
        elif ChosenButton == 2:
            r = Game.Button2()
            Q2_n += 1
            Q2 = Q2+(1/Q2_n)*(r-Q2)
            rewards +=r
        else:
            r = Game.Button3()
            Q3_n += 1
            Q3 = Q3+(1/Q3_n)*(r-Q3)
            rewards += r
    print('values for the 3 buttons',Q1, Q2, Q3)
    return(rewards)

def DecayingRewards(alpha):

    x=np.arange(1, 100)
    y=np.array([])
    for i in range(1,100):
        dummy_reward=50
        y=np.append(y,dummy_reward*alpha*math.pow(1-alpha,i-1))
    plt.plot(x, y)
    plt.xlabel('time')
    plt.ylabel('reward weight')
    plt.legend()
    plt.show()

def EpsilonGreedyActionSelection(epsilon,trials):
    Q1 = 0
    Q2 = 0
    Q3 = 0
    Q1_n = 0
    Q2_n = 0
    Q3_n = 0
    Game = KarmedBandits()
    rewards=0
    for i in range(0, trials):
        percentage=random.random()
        if percentage<=epsilon:
            ChosenButton = random.randint(1, 3)
        else:
            ChosenButton=([Q1,Q2,Q3].index(max([Q1,Q2,Q3])))+1
        if ChosenButton == 1:
            r = Game.Button1()
            Q1_n += 1
            Q1 = Q1+(1/Q1_n)*(r-Q1)
            rewards +=r
        elif ChosenButton == 2:
            r = Game.Button2()
            Q2_n += 1
            Q2 = Q2+(1/Q2_n)*(r-Q2)
            rewards +=r
        else:
            r = Game.Button3()
            Q3_n += 1
            Q3 = Q3+(1/Q3_n)*(r-Q3)
            rewards +=r
    print('values for the 3 buttons',Q1, Q2, Q3)
    return(rewards)

def FreeTrial():
    Game = KarmedBandits()
    print(Game.Button1())
    print(Game.Button2())
    print(Game.Button3())



if __name__ == '__main__':
    #FreeTrial()
    steps=1000
    print(RandomActionSelection(steps))
    print(RandomActionSelectionIUR(steps))
    #DecayingRewards(0.1)
    print(EpsilonGreedyActionSelection(0.1,steps))

    #runs=1000
    #randomPolicyAvg=0
    #EgreedyPolicyAvg=0
    #for i in range(0,runs):
    #    randomPolicyAvg+=RandomActionSelectionIUR(steps)
    #    EgreedyPolicyAvg+=EpsilonGreedyActionSelection(0.1,steps)
    #print("average return for the random policy for",runs,'runs is equal to',randomPolicyAvg/runs)
    #print("average return for the epsilon greedy policy for",runs,'runs is equal to',EgreedyPolicyAvg/runs)



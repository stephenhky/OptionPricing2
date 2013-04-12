'''
Created on Apr 12, 2013

@author: hok1
'''

from StockBinomialTree import StockBinomialTree
import numpy as np

class AmericanCallBinomialTree(StockBinomialTree):
    '''
    Binomial Tree for European call option
    '''


    def __init__(self, S0=1.0, X=0.8, r=0.05, sigma=0.05, T=1.0, no_steps=100):
        '''
        Constructor
        '''
        self.S0 = S0
        self.X = X
        self.r = r
        self.sigma = sigma
        self.T = T
        self.no_steps = no_steps
        
        self.initializeParameters()
        self.initializeStockTree()
        self.initializeOptionPriceTree()
        self.calculateOptionPriceTree()
        
    def calculateOptionPriceTree(self):
        for j in range(self.no_steps+1):
            self.optionPriceTree[self.no_steps][j] = max(self.stockTree[self.no_steps][j]-self.X, 0)
        for i in range(self.no_steps-1, -1, -1):
            for j in range(i+1):
                imValue = self.stockTree[i][j] - self.X
                euroCallValue = np.exp(-self.rdt)*(self.p*self.optionPriceTree[i+1][j]+(1-self.p)*self.optionPriceTree[i+1][j+1])
                self.optionPriceTree[i][j] = max(imValue, euroCallValue)

if __name__ == '__main__':
    amCall = AmericanCallBinomialTree(S0=100, X=105, r=0.05, sigma=1.0, T=4, no_steps=4)
    print amCall.getPrice()
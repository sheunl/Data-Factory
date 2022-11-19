'''
ArrayGenerator generates array of types
'''

from generators.ClassicGenerator import ClassicGenerator
from utilities.Alphanumerics import Alphanumerics
from core.StringGenerator import StringGenerator
import random

class ArrayGenerator(ClassicGenerator):

    def __init__(self,length=10, type='Integer',low=0,high=9) -> None:
        __types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5, 'Integer':6,'Decimal':7, 'Symbolic':8}
        super().__init__(length,'String')
        self.low=low
        self.high=high
    
    def generateInt(self):
        arr=[]
        for x in range(self.length):
            arr.append(random.random(self.low,self.high))
        return arr

    def generateAlphaNumeric(self):
        l=[]
        for i in range(self.length):
            rint=random.randint(self.low,self.high)
            gAN= StringGenerator(rint,'AlphaNumeric')
            l.append(gAN.generate())
        return l
        

    def generateAlphabet(self):
        pass

    def generateAlphabet_Upper(self):
        pass

    def generateAlphabet_Lower(self):
        pass

    def generateAlphaSymbolic(self):
        pass

    def generateInterger(self):
        pass

    def generateDecimal(self):
        pass

    def generateSymbolic(self):
        pass


    def generate(self):
        if self.__type == 1:
            return self.generateInt()
        elif self.__type == 2:
            pass
        elif self.__type == 3:
            pass
        
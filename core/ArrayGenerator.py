'''
ArrayGenerator generates array of types
'''

from generators import ClassicGenerator
import random

class ArrayGenerator(ClassicGenerator):
    def __init__(self,length=10, type='Integer',low=0,high=9) -> None:
        super().__init__(length,type)
        self.low=low
        self.high=high
    
    def generateInt(self):
        arr=[]
        for x in range(self.length):
            arr.append(random.random(self.low,self.high))
        return arr

    def generate(self):
        if self.__type == 1:
            return self.generateInt()
        elif self.__type == 2:
            pass
        elif self.__type == 3:
            pass
        
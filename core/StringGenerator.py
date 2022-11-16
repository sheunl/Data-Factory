from generators.ClassicGenerator import ClassicGenerator
from utilities.Alphanumerics import Alphanumerics
import random

class StringGenerator(ClassicGenerator):

    def __init__(self, length=10,type='Alphabet') -> None:
        __types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5}
        super().__init__(length, 'String')
        self.all=Alphanumerics().alphalower()+Alphanumerics().alphaupper()+Alphanumerics().numeric()
        self.__type=__types[type]
    
    def generateAlphaNumeric(self):
        return random.sample(self.all,self.length)
    
    def generateAlpha(self):
        return random.sample(Alphanumerics().alphalower()+Alphanumerics().alphaupper(),self.length)
    
    def generateAlphabetUpper(self):
        return random.sample(Alphanumerics().alphaupper(),self.length)

    def generateAlphabetLower(self):
        return random.sample(Alphanumerics().alphalower(),self.length)

    def generateAlphabetSymbolic(self):
        return random.sample(Alphanumerics().symbols()+self.all,self.length)

    def generate_list(self):
        if self.__type == 1:
            return self.generateAlphaNumeric()
        elif self.__type == 2:
            return self.generateAlpha()
        elif self.__type == 3:
            return self.generateAlphabetUpper()
        elif self.__type == 4:
            return self.generateAlphabetLower()
        elif self.__type == 5:
            return self.generateAlphabetSymbolic()
    
    def generate(self):
        return ''.join(self.generate_list())
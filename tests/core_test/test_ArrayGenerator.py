import unittest
import random
from core.ArrayGenerator import ArrayGenerator 

class ArrayGeneratorTestMethods(unittest.TestCase):
    def test_AlphaNumericGenerator(self):
        length=random.randint(1,100)
        high=random.randint(50,100)
        low=random.randint(1,50)
        argen=ArrayGenerator(length,'AlphaNumeric',low,high)
        print(argen.generateAlphaNumeric())

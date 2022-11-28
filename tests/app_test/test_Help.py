import unittest
from app.Help import Help

class HelpTestMethods(unittest.TestCase):
    
    def test_noValue(self):
        print("test_noValue")
        Help.noValue()
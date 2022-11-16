import unittest
import random
from generators.ClassicGenerator import ClassicGenerator

class ClassicGeneratorTestMethods(unittest.TestCase):
    def test_default_init(self):
         default = ClassicGenerator()
         self.assertEqual(default.getLength(),10)
         self.assertEqual(default.getType(),1)
    
    def test_defined_init(self):
        __types=['Integer','String','Decimal']
        length=random.randint(0,100)
        dtype=random.randint(1,3)
        defined = ClassicGenerator(length,__types[dtype-1])
        self.assertEqual(defined.getLength(),length)
        self.assertEqual(defined.getType(),dtype)



    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
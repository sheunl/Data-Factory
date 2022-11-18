import os
from themain.Print import Print
class Interactive:
# __types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5}
    def StringGenOptions(self):
        os.system('cls')
        __types=['AlphaNumeric','Alphabet','Alphabet_Upper','Alphabet_Lower', 'AlphaSymbolic']
        print("1. AlphaNumeric")
        print("2. Alphabet")
        print("3. Alphabet_Upper")
        print("4. Alphabet_Lower")
        print("5. AlphaSymbolic")
        ind = input()
        match ind:
            case '1' | '2' |'3' | '4' | '5':
                Print().print_string(__types[int(ind)-1])


    def ArrayGenOptions(self):
        pass

    def start(self):
        print("Hello, Welcome to DataFactory. Below are options. Input number:")
        print("1. String Generation")
        print("2. Array Generation")
        option = input()

        match option :
            case '1':
                self.StringGenOptions()
            case '2':
                self.ArrayGenOptions()
            case other:
                print("Not Available")


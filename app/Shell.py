from app.Help import Help

class Shell:

    def __init__(self) -> None:
        #match input to type
        self.xxarray_types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5, 'Integer':6,'Decimal':7, 'Symbolic':8}
        self.xxstring_types={'AlphaNumeric':1,'Alphabet':2,'Alphabet_Upper':3,'Alphabet_Lower':4, 'AlphaSymbolic':5}
        self.data_type=0
        self.value_type=0
        self.printfile=False
        self.filename='output.txt'

    def parse(self, string):
        self.check_for_errors(string)
        print(self.filename)

    def check_for_errors(self, string):
        if '-s' not in string:
            Help().noValue()

        if '-t' not in string:
            Help().noValue()

        try:
            self.data_type=string[string.index('-t')+1]
            self.value_type=string[string.index('-s')+1]
            if '-x' in string:
                try:
                    self.filename=string[string.index('-x')+1]
                except:
                    pass

                self.printfile=True
        except:
            Help().noValue()

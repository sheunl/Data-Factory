
class Interative:

    def StringGenOptions(self):
        pass

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


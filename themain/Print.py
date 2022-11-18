from inout.Display import Display
from inout.FileGenerator import FileGenerator
from core.StringGenerator import * 
import os
class Print:
    def print_string(self,ind):
        os.system('cls')
        print("Input Length")
        length = input()
        string =  StringGenerator(int(length),ind)
        Display().print_out(string.generate())

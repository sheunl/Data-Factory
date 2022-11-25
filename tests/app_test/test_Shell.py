import unittest
from app.Shell import Shell

class ShellTestMethods(unittest.TestCase):
    
    def test_Commands(self):
        shell = Shell()
        stringlist = "-t a -v n".split()
        with self.assertRaises(TypeError):
            shell.check_for_errors(3)
        # shell.parse(stringlist)
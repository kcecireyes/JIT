import unittest
import os

 
class TextJIT(unittest.TestCase):
    def setUp(self):
    	pass

    def test_say_should_generate_python(self):
        #run test program
        os.system("./jit_cli.py -f programs/program1-five_says.txt")
        match = True
        with open("programs/program1-five_says.py") as ref, open("programs/program1-five_says.gen.py") as output:
            for line1, line2 in zip(ref, output):
                if line1 != line2:
                    print line1
                    print "does not match"
                    print line2
                    match = False
        self.assertTrue(match)

if __name__ == '__main__':
    unittest.main()
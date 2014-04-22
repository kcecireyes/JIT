import unittest
import os

 
class TextJIT(unittest.TestCase):
    def setUp(self):
    	pass

    def test_say_should_generate_python(self):
        #run test program
        prog = "./jit_cli.py -f programs/program1-five_says.txt"
        ref = "programs/program1-five_says.py"
        out = "programs/program1-five_says.gen.py"
        self.assertTrue(self.compare(out, ref, prog))

    def test_listen_should_generate_python(self):
        pass

    def create_node_should_generate_python(self):
        prog = "./jit_cli.py -f programs/program4-simple_node.txt"
        ref = "programs/program4-simple_node.py"
        out = "programs/program4-simple_node.gen.py"
        self.assertTrue(self.compare(out, ref, prog))
        pass

    def test_binop_should_generate_python(self):
        # prog = "./jit_cli.py -f programs/program3-assignments_and_math.txt"
        # ref = "programs/program3-assignments_and_math.txt"
        # out = "programs/program3-assignments_and_math.txt"
        # self.assertTrue(self.compare(out, ref, prog))
        pass

    def compare(self, out, ref, prog):
        os.system(prog)
        match = True
        with open(ref) as ref, open(out) as output:
            for line1, line2 in zip(ref, output):
                if line1 != line2:
                    print line1
                    print "does not match"
                    print line2
                    match = False
        return match

if __name__ == '__main__':
    unittest.main()
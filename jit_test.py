import unittest
import os

 
class TextJIT(unittest.TestCase):
    def setUp(self):
        self.jit = "./jit_cli.py"
        self.flag = "--silent -f"
        self.prog_ext = ".txt"
        self.ref_ext = ".py"
        self.out_ext = ".gen.py"

        # Add programs here
        self.program0 = "programs/program0-one_says"
        self.program1 = "programs/program1-five_says"
        self.program2 = "programs/program2-nodes"
        self.program3 = "programs/program3-assignments_and_math"
        self.program4 = "programs/program4-simple_node"
        self.program5 = "programs/program5-simple_variable"
        self.program6 = "programs/program6-blocks"
        self.program7 = "programs/program7-pushing_and_pulling"
        self.program9 = "programs/program9-saving_and_stuff"
        self.program11 = "programs/program11-forloops_and_blocks"

    def test_comments_should_be_parsed_out(self):
        self.assertTrue(self.compare(self.program0))

    def test_say_should_generate_python(self):
        self.assertTrue(self.compare(self.program1))

    def test_listen_should_generate_python(self):
        self.assertTrue(self.compare(self.program2))

    def test_binop_should_generate_python(self):
        self.assertTrue(self.compare(self.program3))

    def test_simple_node_should_generate_python(self):
        self.assertTrue(self.compare(self.program4))

    def test_should_assign_variables(self):
        self.assertTrue(self.compare(self.program5))  

    def test_should_allow_blocks(self):
        self.assertTrue(self.compare(self.program6))  

    def test_pushing_and_pulling(self):
        self.assertTrue(self.compare(self.program7))

    def test_should_save_and_import(self):
        self.assertTrue(self.compare(self.program9))  

    def test_should_forloops_and_blocks(self):
        self.assertTrue(self.compare(self.program11))  

    def compare(self, program):
        prog = self.jit + " " + self.flag + " " + program + self.prog_ext
        ref = program + self.ref_ext
        out = program + self.out_ext

        print "beginning test: " + prog
        os.system(prog)
        match = True
        with open(ref) as ref, open(out) as output:
            for line1, line2 in zip(ref, output):
                if line1 != line2:
                    print line1
                    print "does not match"
                    print line2
                    match = False
        print "Finished test: " + prog
        return match

if __name__ == '__main__':
    unittest.main()

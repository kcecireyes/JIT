import unittest
import os

 
class TextJIT(unittest.TestCase):
    def setUp(self):
        self.jit = "./jit_cli.py"
        self.flag = "-f"
        self.prog_ext = ".txt"
        self.ref_ext = ".py"
        self.out_ext = ".gen.py"
        self.program1 = "programs/program1-five_says"
        self.program2 = ""
        self.program3 = "programs/program3-assignments_and_math"
        self.program4 = "programs/program4-simple_node"
        self.program5 = ""

    def test_say_should_generate_python(self):
        prog = self.jit + " " + self.flag + " " + self.program1 + self.prog_ext
        ref = self.program1 + self.ref_ext
        out = self.program1 + self.out_ext
        self.assertTrue(self.compare(out, ref, prog))

    def test_listen_should_generate_python(self):
        pass

    def create_node_should_generate_python(self):
        prog = self.jit + " " + self.flag + " " + self.program2 + self.prog_ext
        ref = self.program4 + self.ref_ext
        out = self.program4 + self.out_ext
        self.assertTrue(self.compare(out, ref, prog))
        pass

    def test_binop_should_generate_python(self):
        # prog = jit + " " + flag + " " + program3 + prog_ext
        # ref = program3 + ref_ext
        # out = program3 + out_ext
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
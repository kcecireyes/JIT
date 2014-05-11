import unittest
import os


class TextJIT(unittest.TestCase):
    def setUp(self):
        self.jit = "./jit_cli.py"
        self.flag = "-f"
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
        self.program10 = "programs/program10-scope_blocks"
        self.program11 = "programs/program11-forloops_and_blocks"
        self.program12 = "programs/program12-search"
        self.program13 = "programs/program13-if_else"
        self.program14 = "programs/program14-nested_forloops"
        self.program15 = "programs/program15-nested-if-else"
        self.program16 = "programs/program16-operations"
        self.program17 = "programs/program17-function_declarations"
        self.the_last_program = "programs/test_program_to_end_all_programs"

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

    def test_should_scope_and_block(self):
        self.assertTrue(self.compare(self.program10)) 

    def test_should_forloops_and_blocks(self):
        self.assertTrue(self.compare(self.program11))

    def test_should_test_search_func(self):
        self.assertTrue(self.compare(self.program12))   

    def test_if_and_else(self):
        self.assertTrue(self.compare(self.program13)) 

    def test_nesting(self):
        self.assertTrue(self.compare(self.program14)) 

    def test_nested_if_else(self):
        self.assertTrue(self.compare(self.program15)) 

    def test_operations(self):
        self.assertTrue(self.compare(self.program16)) 

    def test_function_declarations(self):
        self.assertTrue(self.compare(self.program17)) 

    def test_the_universe(self):
        self.assertTrue(self.compare(self.the_last_program)) 

    def compare(self, program):
        match = True
        name = program
        prog = self.jit + " " + self.flag + " " + program + self.prog_ext
        ref = program + self.ref_ext
        out = program + self.out_ext

        print "\n>> beginning test: " + name
        os.system(prog)
        if not open(ref).read():
            print "***************no gen file************************"
            match = False
            return match

        ref_lines = []
        out_lines = []
        with open(ref) as ref, open(out) as out:
            ref_lines = ref.readlines()
            out_lines = out.readlines()
            out_lines = out_lines[10:]

        for line1, line2 in zip(ref_lines, out_lines):
            if line1 != line2:
                print ">\""+line1+"\"<",
                print " does not match ",
                print ">\""+line2+"\"<"
                match = False

        print "\n>> Finished test: " + name
        return match

if __name__ == '__main__':
    unittest.main()

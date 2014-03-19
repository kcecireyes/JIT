#!/usr/bin/python
from optparse import OptionParser
import glob

class Program:
	code = ""
	
	def __init__(self, path):
		print path+":"
		code = open(path, 'r')
		for line in code:
			print "\t"+line
		print "\n"

def main():
	parser = OptionParser()
	parser.add_option("-f", "--file", dest="filename", help="JIT program filename", type="string")
	(options, args) = parser.parse_args() 

	if (options.filename):
		prog = Program(options.filename)
	else:
		# Compile everything in this folder
		for fname in glob.glob('*.jit'):
			prog = Program(fname)

if __name__ == '__main__':
    main()

#!/usr/bin/python
import os.path, sys
sys.path.append("/Users/rkuykendall/Dropbox/Code/JIT")
import jitlib

print '\n'.join(["Beginning node program."])
myNode = Node()
myNode.title = "The Never-Ending Controversy Over All-Girls Education"
myNode.author = "CHRISTINE GROSS-LOH"
print '\n'.join([myNode.author])
myNode.author = Listen()
myNode.date = "March 21 2014"
myNode.publisher = "The Atlantic"
myNode.keywords = ["girls", "education", "debate",]
myNode.body = "string_body"

#!/usr/bin/python
import os.path, sys
sys.path.append("/Users/rkuykendall/Dropbox/Code/JIT")
import jitlib

print '\n'.join(["Beginning push program."])
myNode = Node()
myNode2 = Node()
myNode3 = Node()
myNode4 = Node()
print '\n'.join([myNode.author])
push(myNode)
myCollection = [myNode2, myNode3, myNode4,]
push(myCollection)
push(myNode, myCollection)

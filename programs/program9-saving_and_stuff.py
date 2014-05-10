#!/usr/bin/python
import os.path, sys
sys.path.append("/Users/rkuykendall/Dropbox/Code/JIT")
import jitlib

myFile = "file.txt"
json = "filename.json"
myNode = Node()
myNode3 = Node()
myNode4 = Node()
myNode.body = import("file.txt")
myNode.body = import(myFile)
save(myNode)
myNode3 = get("filename.json")
myNode4 = get(json)

#!/usr/bin/python
# Be sure to add jitlib to your path!
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

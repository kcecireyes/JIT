print '\n'.join(["Beginning node program."])
myNode = Node()
myNode.title = "The Never-Ending Controversy Over All-Girls Education"
myNode.author = "CHRISTINE GROSS-LOH"
print '\n'.join([myNode.author])
myNode.author = raw_input()
myNode.date = "March 21 2014"
myNode.publisher = "The Atlantic"
myNode.set_keywords(["girls", "education", "debate",])
myNode.body = "string_body"

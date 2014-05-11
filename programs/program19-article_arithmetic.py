x.keywords = list(set(myNode1.keywords) | set(myNode2.keywords))
x.keywords = list(set(myNode1.keywords) & set(myNode2.keywords))
x.keywords = list(set(myNode1.keywords) | set(myNode2.keywords))
x.keywords = list(set(myNode1.keywords) | set(myNode2.keywords))
x.title = myNode1.title + ', ' + myNode2.title
x.keywords = list(set(myNode1.keywords) & set(myNode2.keywords))
x.date = list(set(myNode1.date.split('/')) & set(myNode2.date.split('/')))
x.body = list(set(myNode1.body) & set(myNode2.body))
x.publisher = myNode1.publisher if myNode1.publisher == myNode2.publisher else ''
x.author = myNode1.author if myNode1.author == myNode2.author else ''

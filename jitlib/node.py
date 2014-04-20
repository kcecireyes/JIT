class Node():
    # title, author, date, publisher, body, publisher, keywords

    def __init__(self, title=None, author=None, publisher=None, body=None):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.body = body
        self.keywords = []
        self.adjacencies = []

    def set_keywords(self, value):
    	if type(value) is list:
    		keywords.extend(value)
    	else:
    		keywords.append(value)

    def set_body(self, value, flag=None):
    	if flag == "f":
    		with open(value) as file:
    			for line in file:
    				body += line
    	else:
    		body = value

    def add_keywords(self, value):
		if type(value) is list:
			self.keywords.extend(value)
		else:
			self.keywords.append(value) 

    def add_body(self, value, flag=None):
		self.body = ""
		if flag == "f":
			with open(value) as file:
				for line in file:
					self.body += line
		else:
			self.body = value

    def add_adjacent(self, value):
		value.adjacencies.append(self)
		self.adjacencies.append(value)


    keywords = property(set_keywords)
    body = property(set_body)


from database import Base

class Keyword(Base):
    __tablename__ = 'keywords'
    value = Column(String)

    __init_(self, value):
        self.value = value

class Node(Base):
    __tablename__ = 'nodes'

    title = Column(String)
    author = Column(String)
    publisher = Column(String)
    body = Column(String)
    # keywords
    # adjacencies

    # places = Column(TextPickleType(pickler=json))
    # sentiment = Column(Integer)
    # last_referenced = Column(DateTime, default=datetime.datetime.now)

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

    def add_adjacent(self, node):
        if node not in self.adjacencies:
            self.adjacencies.append(node)
        else:
            return False

    def get_adjacencies(self):
        return self.adjacencies


    keywords = property(set_keywords)
    body = property(set_body)

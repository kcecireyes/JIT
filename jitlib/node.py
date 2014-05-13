from sqlalchemy import MetaData, Table, Column, Integer, ForeignKey, DateTime, String
from sqlalchemy.orm import mapper, relationship
from database import Base, session
import datetime
import json

node_keywords_table = Table('node_keywords', Base.metadata,
    Column('node_id', Integer, ForeignKey('node.id')),
    Column('keyword_id', Integer, ForeignKey('keyword.id'))
)

def node_get(filename):
    try:
        with open(filename, 'r') as f:
            v = json.loads(f.read())
            return Node(title = v['title'], author = v['author'],
                        publisher = v['publisher'], body = v['body'])
    except IOError:
        return Node()

class Node(Base):
    __tablename__ = 'node'

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    title = Column(String(255))
    author = Column(String(255))
    date = Column(DateTime)
    publisher = Column(String(255))
    body = Column(String(255))
    # Adjacencies
    keywords = relationship("Keyword",
                            secondary=node_keywords_table,
                            backref="nodes")

    def __init__(self, title="", author="", publisher="", body=""):
        # title, author, date, publisher, body, publisher, keywords
        self.title = title
        self.author = author
        self.publisher = publisher
        self.body = body

    def push(self):
        session.add(self)
        session.commit()
        pass

    def set_keywords(self, value):
        if type(value) is list:
            for v in value:
                self.keywords.append(Keyword(v))
        else:
            self.keywords.append(Keyword(value))

    def set_body(self, value, flag=None):
    	if flag == "f":
    		with open(value) as file:
    			for line in file:
    				body += line
    	else:
    		body = value

    def add_keywords(self, value):
        if len(value) < 1:
            return

        if type(value) is list:
            for v in value:
                self.keywords.append(Keyword(v))
        else:
            self.keywords.append(Keyword(value))

    def add_body(self, value, flag=None):
		self.body = ""
		if flag == "f":
			with open(value) as file:
				for line in file:
					self.body += line
		else:
			self.body = value

    def add_adjacencies(self, *nodes):
        for node in nodes:
            if node not in self.adjacencies():
                Edge(self, node)
        return self

    def add_adjacent(self, node):
        '''Do not use this method. Use add_adjacencies(node) instead.'''
        self.add_adjacencies(node)

    def adjacencies(self):
        all_nodes = [x.lower_node for x in self.higher_edges]
        all_nodes.extend([x.higher_node for x in self.lower_edges])
        return all_nodes

    def save(self, filename=""):
        if filename == "":
            if self.id != None:
                filename = str(self.id) + ".node"
            else:
                filename = "no_id.node"

        with open(filename, 'w') as f:
            f.write(json.dumps({"title": self.title, "author": self.author,
                                "publisher": self.publisher, "body": self.body},
                                sort_keys=True))

class Keyword(Base):
    __tablename__ = 'keyword'

    id = Column(Integer, primary_key=True)
    value = Column(String(255))

    def __new__(cls, *args, **kwargs):
        if len(args) > 0:
            query = session.query(Keyword).filter_by(value = args[0]).first()
            if query != None:
                return query
            else:
                return Base.__new__(cls, *args, **kwargs)

    def __init__(self, val):
        self.value = val
        session.add(self)

class Edge(Base):
    __tablename__ = 'edge'

    lower_id = Column(Integer,
                        ForeignKey('node.id'),
                        primary_key=True)

    higher_id = Column(Integer,
                        ForeignKey('node.id'),
                        primary_key=True)

    lower_node = relationship(Node,
                                primaryjoin=lower_id==Node.id,
                                backref='lower_edges')
    higher_node = relationship(Node,
                                primaryjoin=higher_id==Node.id,
                                backref='higher_edges')

    # here we have lower.id <= higher.id
    def __init__(self, n1, n2):
        if n1.id < n2.id:
            self.lower_node = n1
            self.higher_node = n2
        else:
            self.lower_node = n2
            self.higher_node = n1

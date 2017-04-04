
from py2neo import Graph

graph = Graph(password="password")

shows = ['DareDevil', 'Jessica Jones', 'Luke Cage', 'Iron Fist']

for show in shows:
    graph.run("CREATE (s:Show {name:{S}}) RETURN s", {"S": show})

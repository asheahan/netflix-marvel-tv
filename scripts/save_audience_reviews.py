
import json
from py2neo import Graph

graph = Graph(password="password")

with open('data/daredevil/audience-reviews.json', 'r') as handle:
    DD_AUDIENCE_REVIEWS = json.load(handle)

with open('data/jessica-jones/audience-reviews.json', 'r') as handle:
    JJ_AUDIENCE_REVIEWS = json.load(handle)

with open('data/luke-cage/audience-reviews.json', 'r') as handle:
    LC_AUDIENCE_REVIEWS = json.load(handle)

with open('data/iron-fist/audience-reviews.json', 'r') as handle:
    IF_AUDIENCE_REVIEWS = json.load(handle)

AUDIENCE_REVIEWS = DD_AUDIENCE_REVIEWS + JJ_AUDIENCE_REVIEWS + LC_AUDIENCE_REVIEWS + IF_AUDIENCE_REVIEWS

# users = {}
# for review in AUDIENCE_REVIEWS:
#     if review['user_id'] not in users.items():
#         users[review['user_id']] = review['user_name']

# for user, name in users.items():
#     graph.run("CREATE (u:User {id: {i}, name:{n}}) RETURN u", {"i": user, "n": name})

for review in AUDIENCE_REVIEWS:
    graph.run("MATCH (u:User), (s:Show) WHERE u.id = {i} AND s.name = {sh} CREATE (u)-[r:REVIEWED {date: {d}, season: {se}, rating: {ra}, review: {re}}]->(s) RETURN r", 
        {"i": review['user_id'], "sh": review['show'], "d": review['date'], "se": review['season'], "ra": review['rating'], "re": review['body']})

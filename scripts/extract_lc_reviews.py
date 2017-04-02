
import codecs
import glob
import json
from bs4 import BeautifulSoup

def get_ratings(row):
    stars = float(len(row.select("span.glyphicon-star")))
    if len(row.text.strip()) > 0:
        stars += .5
    return stars

critic_reviews = []
audience_reviews = []

for season in range(1, 2):
    for file in glob.glob('data/luke-cage/rottentomatoes/critic-reviews-season-' \
        + str(season) + '-*'):
        with open(file, 'r') as handle:
            soup = BeautifulSoup(handle, "html.parser")
            for row in soup.select("div.review_table_row"):
                review = {}
                review['show'] = 'Luke Cage'
                review['season'] = str(season)
                review['user_id'] = row.select("div.critic_name a")[0].get("href").replace("/critic/", "").replace("/", "")
                review['user_name'] = row.select("div.critic_name a")[0].text.strip()
                review['source'] = row.select("div.critic_name a")[1].text.strip()
                review['date'] = row.select("div.review_date")[0].text.strip()
                review['body'] = row.select("div.the_review")[0].text.strip()
                print(review['user_id'])
                critic_reviews.append(review)

    for file in glob.glob('data/luke-cage/rottentomatoes/audience-reviews-season-' \
        + str(season) + '-*'):
        with open(file, 'r') as handle:
            soup = BeautifulSoup(handle, "html.parser")
            for row in soup.select("div.review_table_row"):
                if len(row.select("span.fl")) > 0:
                    review = {}
                    review['show'] = 'Luke Cage'
                    review['season'] = str(season)
                    review['rating'] = get_ratings(row.select("span.fl")[0])
                    review['user_id'] = row.select("div.critic_name a")[0].get("href").replace("/user/id/", "").replace("/", "")
                    review['user_name'] = row.select("div.critic_name a")[0].text.strip()
                    review['date'] = row.select("span.fr")[0].text.strip() \
                        if len(row.select("span.fr")) > 0 else ""
                    review['body'] = row.select("div.user_review")[0].text.strip() \
                        if len(row.select("div.user_review")) > 0 else ""
                    print(review['user_id'])
                    audience_reviews.append(review)

with codecs.open('data/luke-cage/critic-reviews.json', 'w', 'utf-8') as handle:
    json.dump(critic_reviews, handle)
with codecs.open('data/luke-cage/audience-reviews.json', 'w', 'utf-8') as handle:
    json.dump(audience_reviews, handle)

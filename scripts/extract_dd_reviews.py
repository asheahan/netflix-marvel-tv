
import glob
from bs4 import BeautifulSoup

for season in range(1, 3):
    for file in glob.glob('data/daredevil/rottentomatoes/critic-reviews-season-' \
        + str(season) + '-*'):
        with open(file, 'r') as handle:
            soup = BeautifulSoup(handle, "html.parser")
            for row in soup.select("div.review_table_row"):
                review = {}
                review['show'] = 'DareDevil'
                review['season'] = str(season)
                review['author'] = row.select("div.critic_name a")[0].text.strip()
                review['source'] = row.select("div.critic_name a")[1].text.strip()
                review['date'] = row.select("div.review_date")[0].text.strip()
                review['body'] = row.select("div.the_review")[0].text.strip()
                print(review)

    for file in glob.glob('data/daredevil/rottentomatoes/audience-reviews-season-' \
        + str(season) + '-*'):
        with open(file, 'r') as handle:
            soup = BeautifulSoup(handle, "html.parser")
            for row in soup.select("div.review_table_row"):
                review = {}
                review['show'] = 'DareDevil'
                review['season'] = str(season)
                review['author'] = row.select("div.critic_name a")[0].text.strip()


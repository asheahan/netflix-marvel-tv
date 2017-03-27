
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

episodes = { }
for season in range(1, 3):
    episode_list = open("data/daredevil/season-" + str(season), 'r')
    soup = BeautifulSoup(episode_list.read(), "html.parser")

    for row in soup.select("div.list_item"):
        episode_number = row.select("div.image div div")[0].text
        uri = row.select("div.info a")[0].get("href")
        episodes[episode_number] = urlparse(uri)[2]

for key, value in episodes.items():
    key = key.replace(", ", "-")
    filename = "data/daredevil/imdb/" + key
    with open(filename, 'wb') as handle:
        file = "http://www.imdb.com" + value
        response = requests.get(file, stream=True)

        if response.status_code == requests.codes.ok:
            handle.write(response.content)

    with open(filename + "-fullcredits", 'wb') as handle:
        file = "http://www.imdb.com" + value + "fullcredits"
        response = requests.get(file, stream=True)

        if response.status_code == requests.codes.ok:
            handle.write(response.content)

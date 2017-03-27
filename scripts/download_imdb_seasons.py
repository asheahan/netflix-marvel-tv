
import requests

shows = {
    'daredevil': {
        'seasons': 2,
        'imdb_id': 'tt3322312'
    },
    'jessica-jones': {
        'seasons': 1,
        'imdb_id': 'tt2357547'
    },
    'luke-cage': {
        'seasons': 1,
        'imdb_id': 'tt3322314'
    },
    'iron-fist': {
        'seasons': 1,
        'imdb_id': 'tt3322310'
    }
}

for name, info in shows.items():
    for season in range(1, info['seasons'] + 1):
        filename = "data/" + name + "/season-" + str(season)
        with open(filename, 'wb') as handle:
            file = "http://www.imdb.com/title/" + \
                info['imdb_id'] + "/episodes?season=" + str(season)
            response = requests.get(file, stream=True)

            if response.status_code == requests.codes.ok:
                handle.write(response.content)



import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# -- Critics --
for season in range(1, 2):
    num_pages = 1
    filename = "data/jessica-jones/rottentomatoes/critic-reviews-season-" + str(season) + "-1"
    with open(filename, 'wb') as handle:
        file = "https://www.rottentomatoes.com/tv/jessica_jones/s0" + \
            str(season) + "/reviews"
        response = requests.get(file, stream=True)

        if response.status_code == requests.codes.ok:
            handle.write(response.content)

        soup = BeautifulSoup(response.content, "html.parser")
        page_info = soup.select("div#reviews div.content div span.pageInfo")[0].text
        num_pages = int(page_info[page_info.index("of") + 3:])
        # num_pages = int(soup.select("div#reviews div.content div span.pageInfo")[0].text[-1])

    if num_pages > 1:
        for page in range(2, num_pages + 1):
            filename = "data/jessica-jones/rottentomatoes/critic-reviews-season-" \
                + str(season) + "-" + str(page)
            with open(filename, 'wb') as handle:
                file = "https://www.rottentomatoes.com/tv/jessica_jones/s0" + \
                    str(season) + "/reviews?page=" + str(page)
                response = requests.get(file, stream=True)

                if response.status_code == requests.codes.ok:
                    handle.write(response.content)

# -- Audience --
for season in range(1, 2):
    num_pages = 1
    filename = "data/jessica-jones/rottentomatoes/audience-reviews-season-" + str(season) + "-1"
    with open(filename, 'wb') as handle:
        file = "https://www.rottentomatoes.com/tv/jessica_jones/s0" + \
            str(season) + "/reviews/?type=user"
        response = requests.get(file, stream=True)

        if response.status_code == requests.codes.ok:
            handle.write(response.content)

        soup = BeautifulSoup(response.content, "html.parser")
        page_info = soup.select("div#reviews div.inlineBlock span.pageInfo")[0].text
        num_pages = int(page_info[page_info.index("of") + 3:])
        # num_pages = int(soup.select("div#reviews div.inlineBlock span.pageInfo")[0].text[-1])

    if num_pages > 1:
        for page in range(2, num_pages + 1):
            filename = "data/jessica-jones/rottentomatoes/audience-reviews-season-" \
                + str(season) + "-" + str(page)
            with open(filename, 'wb') as handle:
                file = "https://www.rottentomatoes.com/tv/jessica_jones/s0" + \
                    str(season) + "/reviews?page=" + str(page) + "&type=user"
                response = requests.get(file, stream=True)

                if response.status_code == requests.codes.ok:
                    handle.write(response.content)

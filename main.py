import requests
from bs4 import BeautifulSoup
import pprint
# response from website
response = requests.get('https://news.ycombinator.com/news')
# parsed html from response
soup = BeautifulSoup(response.text, 'html.parser')
# saved links using class(.) titlelink, be sure to inspect website to see wat element to grab
links = soup.select('.titlelink')
# get all votes from class(.)score
subtext = soup.select('.subtext')


def sort_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)

def create_custom_hacknews(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        vote = subtext[i].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hacknews(links, subtext))
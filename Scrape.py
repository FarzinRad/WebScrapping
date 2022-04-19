import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
Soup = BeautifulSoup(res.text, 'html.parser')

links = Soup.select('.titlelink')
subtext = Soup.select('.subtext')


def sorting_news(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_func(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        votes = subtext[idx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'links': href, 'votes': points})

    return sorting_news(hn)


pprint.pprint(create_custom_func(links, subtext))

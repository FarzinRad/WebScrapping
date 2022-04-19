import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
Soup = BeautifulSoup(res.text, 'html.parser')

links = Soup.select('.titlelink')
votes = Soup.select('.score')
print(votes[0].get('id'))


def create_custom_hn(links, votes):
    hn[]


return hn

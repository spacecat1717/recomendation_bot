from requests_html import HTMLSession
import requests
import pandas as pd
import unicodedata

session = HTMLSession()

r = session.get('https://www.100bestbooks.ru/')
table = r.html.find('.t-check')
authors = []
titles = []
tmp = []

for t in table:
    new = t.text.split('—')
    a = unicodedata.normalize("NFKD",new[0])
    authors.append(a)
    t = unicodedata.normalize("NFKD", new[1])
    titles.append(t)
    print(authors, titles)



from requests_html import HTMLSession
import requests
import pandas as pd
import unicodedata


class Parser():
    def __init__(self):
        self.session = HTMLSession()

    def parse(self, url:str, selector:str) -> str:
        r = self.session.get(url)
        table = r.html.find(selector)
        return table

class SaveLists():

    def create_lists(self, parsed_text):
        authors = []
        titles = []
        for t in parsed_text:
            new = t.text.split('—')
            a = unicodedata.normalize("NFKD",new[0])
            authors.append(a)
            t = unicodedata.normalize("NFKD", new[1])
            titles.append(t)
        return authors, titles

class SaveExcel():
    
    def save_excel(self, data:tuple):
        df = pd.DataFrame({'Author': data[0],
                        'Title': data[1]})
        df.to_excel('./books.xlsx')
        print('Saved!')


class Main():

    def __init__(self):
        self.parser = Parser()
        self.save = SaveLists()
        self.save_excel = SaveExcel()

    def main(self, url, selector):
        text = self.parser.parse(url, selector)
        lists = self.save.create_lists(text)
        self.save_excel.save_excel(lists)
        


if __name__ == '__main__':
    m = Main()
    m.main('https://www.100bestbooks.ru/', '.t-check')




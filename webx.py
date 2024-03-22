import sys
import requests
from bs4 import BeautifulSoup

class WebBrowser:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
    
    def navigate(self, url=None):
        if url is None:
            url = self.url
        response = self.session.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        tree = soup.find('tree').encode()
        table = soup.find('table').encode()
        print("Tree:", tree)
        print("Table:", table)
    
    def list(self):
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        features = []
        for element in soup.find_all('a'):
            if element.has_attr('href'):
                href = element['href']
                text = element.text
                features.append((href, text))
        print("Features:")
        for feature in features:
            print(feature[0], "|", feature[1])
    
    def source_code(self):
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Source Code:")
        print(soup.prettify())
    
    def exit(self):
        sys.exit()

def main():
    url = input("Enter URL: ")
    browser = WebBrowser(url)
    while True:
        command = input("Enter a command (l for list, s for source code, q to quit, U to navigate to a new URL): 
").lower()
        if command == 'l':
            browser.list()
        elif command == 's':
            browser.source_code()
        elif command == 'q':
            browser.exit()
        elif command == 'u':
            new_url = input("Enter new URL: ")
            browser.navigate(new_url)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

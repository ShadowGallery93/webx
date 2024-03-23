import requests
from bs4 import BeautifulSoup
import sys

class WebBrowser:
    def __init__(self, url):
        self.url = url
        self.session = requests.Session()
        self.features = []

    def list(self):
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.features = []
        for link in soup.find_all('a'):
            href = link.get('href')
            text = link.text
            self.features.append((href, text))
        print("Features:")
        for i, feature in enumerate(self.features):
            print(i, "|", feature[1])

    def source_code(self):
        response = self.session.get(self.url)
        soup = BeautifulSoup(response.content, 'html.parser')
        print("Source Code:")
        print(soup.prettify())

    def exit(self):
        sys.exit()

    def navigate(self, new_url):
        self.url = new_url

    def select(self, index):
        self.navigate(self.features[index][0])

def main():
    url = input("Enter URL: ")
    browser = WebBrowser(url)
    while True:
        command = input("Enter a command (l for list, s for source code, q to quit, u to navigate to a new URL, n to select a link by its number): ")
        if command == 'l':
            browser.list()
        elif command == 's':
            browser.source_code()
        elif command == 'q':
            browser.exit()
        elif command == 'u':
            new_url = input("Enter new URL: ")
            browser.navigate(new_url)
        elif command == 'n':
            index = int(input("Enter the number of the link: "))
            browser.select(index)
        else:
            print("Invalid command")

if __name__ == "__main__":
    main()

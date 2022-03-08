import os
import time
import requests
import validators
from bs4 import BeautifulSoup

"""
Currently made to search for items in stock at Zara

Example Link: https://www.zara.com/us/en/plaid-blazer-p02010745.html
"""


def main():
    headers = {
        'user-agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    print("Email Stock Notifier for Zara")
    url = input("Input the url for the item: ")
    validateUrl(url)
    size = input("Input the size of the item (xs/s/m/l/xl): ")
    validateSize(size)
    while True:
        response = requestURL(
            headers, url)
        soup = getSoup(response)
        entry = findElement(
            soup, "span", "product-detail-size-info__main-label")
        if determineStock(entry):
            print("The Product is in stock")
            os.system('python3 emailNotifier.py ' + url)
            break
        else:
            print("The product is out of stock")
        time.sleep(60)


def validateUrl(url):
    if not validators.url(url):
        print("Not a valid URL")
        exit()
    if not url.find("zara"):
        print("Not a zara link")
        exit()


def validateSize(size):
    valid = False
    if 0 < len(size) < 4:
        valid = True

    if size.lower() == "xs" or size.lower() == "s" or size.lower() == "m" or size.lower() == "l" or size.lower() == "xl" or size.lower() == "xl":
        valid = True
    else:
        valid = False

    if valid == False:
        print("Not a valid size")
        exit()


def requestURL(headers, url):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response
    else:
        print("URL was not able to be requested")
        exit()


def getSoup(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def findElement(soup, htmlElement, classEntry):
    divs = soup.find_all(
        htmlElement, {"class": classEntry})
    for entries in divs:
        if entries.getText() == "M":
            entry = entries
            return entry
    print("The Element was not found")
    exit()


def determineStock(entry):
    parent = entry.parent.parent.parent
    stringParent = str(parent)
    if (stringParent.find('out-of-stock') != -1):
        return False
    else:
        return True


if __name__ == "__main__":
    main()

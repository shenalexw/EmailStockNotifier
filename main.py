import os
import time
import requests
import validators
from dotenv import load_dotenv
from bs4 import BeautifulSoup

"""
Currently made to search for items in stock at Zara

Example Link: https://www.zara.com/us/en/plaid-blazer-p02010745.html
"""
load_dotenv()

# Constants
HEADERS = {
    'user-agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
}

DICTSIZE = {
    "1": "xs",
    "2": "s",
    "3": "m",
    "4": "l",
    "5": "xl",
    "6": "xxl"
}

DEFAULTINPUTS = {
    "url": "https://www.zara.com/us/en/plaid-blazer-p02010745.html",
    "size": "M",
    "timer": 20,
    "email": os.getenv('RECEIVER')
}


def main():
    print("""\
    =====================================
    |                                   |
    |      Zara in-stock Notifier       |
    |                                   |
    =====================================

    1 : Yes
    2 : No
    """)
    default = input("Would you like to run the default inputs? (1 - 2): ")
    validateDefault(default)
    default = convertDefault(default)
    if default:
        url = DEFAULTINPUTS["url"]
        size = DEFAULTINPUTS["size"]
        timer = DEFAULTINPUTS["timer"]
        email = DEFAULTINPUTS["email"]
    else:
        url = input("Input the url for the item: ")
        validateUrl(url)
        print("""\

        1 : XS
        2 : S
        3 : M
        4 : L
        5 : XL
        6 : XXL
        """)
        size = input("Input the size of the item (1 - 6): ")
        validateSize(size)
        size = convertSize(size, DICTSIZE)

        timer = input("Input the timer to refresh the item (1 - 60 seconds): ")
        validateTimer(timer)
        timer = int(timer)

        email = input(
            "Input the email you wish to recieve a notification once the product is in stock (email@gmail.com): ")
        validateEmail(email)

    displayItem = True
    while True:
        response = requestURL(
            HEADERS, url)
        soup = getSoup(response)
        if displayItem:
            print("")
            item = findItem(soup,
                            "h1", "product-detail-info__header-name")
            print("Searching for... " + item)
            print("The process will continue to refresh every " +
                  str(timer) + " seconds")
            print("Press and hold ctrl + c to end the loop")
            displayItem = False

        entry = findElement(
            soup, "span", "product-detail-size-info__main-label", size)
        if determineStock(entry):
            print("The Product is in stock")
            os.system('python3 emailNotifier.py ' + email + ' ' + url)
            break
        else:
            print("The " + item + " is out of stock in size: " + size.upper())
        time.sleep(timer)


def validateDefault(default):
    valid = True
    if len(default) != 1:
        valid = False

    if 0 > int(default) > 1:
        valid = False

    if not valid:
        print("not a valid choice")
        exit()


def validateUrl(url):
    if not validators.url(url):
        print("Not a valid URL")
        exit()
    if not url.find("zara"):
        print("Not a zara link")
        exit()


def validateSize(size):
    valid = True
    if len(size) != 1:
        valid = False

    if 1 > int(size) > 6:
        valid = False

    if not valid:
        print("Not a valid size")
        exit()


def validateTimer(timer):
    valid = True
    if 0 > len(timer) > 2:
        valid = False

    if 1 > int(timer) > 60:
        valid = False

    if not valid:
        print("Not a valid time")
        exit()


def validateEmail(email):
    if not validators.email(email):
        print("Not a valid Email")
        exit()


def convertSize(size, dictSize):
    return dictSize[size]


def convertDefault(default):
    if int(default) == 1:
        return True
    return False


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


def findItem(soup, htmlElement, classEntry):
    item = soup.find(htmlElement, {"class": classEntry})
    return item.getText()


def findElement(soup, htmlElement, classEntry, size):
    divs = soup.find_all(
        htmlElement, {"class": classEntry})
    for entries in divs:
        if entries.getText() == size.upper():
            entry = entries
            return entry
    print("Size not found")
    exit()


def determineStock(entry):
    parent = entry.parent.parent.parent
    print(parent)
    stringParent = str(parent)
    if (stringParent.find('out-of-stock') != -1):
        return False
    else:
        return True


if __name__ == "__main__":
    main()

# Email In-Stock Notifier ✉️

## Table of Contents
- [Abstract](#Abstract)
- [How To Use](#how-to-use)
- [Downloads](#downloads)
- [References](#references)
- [Author(s)](#author-info)

## Abstract
This project was created in order to recieve an email once a product is in stock.

Note: This project only works for products from Zara

## How To Use
- Download Python 3
- Install all packages found in the Downloads section
- Clone the repository to desired directory.
- Create a .env file in the root directory with the following variables for a non secure gmail account to send emails from as recommended by [RealPython: How to send an email using Python](https://realpython.com/python-send-email/).
```
    USERNAME = sendfromthisemail@gmail.com
    PASSWORD = foobar
    RECEIVER = notifythisemail@gmail.com
```
- Open terminal and navigate to the root directory
- In terminal, input the following command.
```
    python3 main.py
```
- The program will welcome you and ask the user for inputs
```
    =====================================
    |                                   |
    |      Zara in-stock Notifier       |
    |                                   |
    =====================================

    1 : Yes
    2 : No
    
Would you like to run the default inputs? (1 - 2): 
```
- If the user inputs 1 for Yes, the program will start automatically using the DEFAULTINPUTS dictionary at the beginning of main.
```
DEFAULTINPUTS = {
    "url": "https://www.zara.com/us/en/plaid-blazer-p02010745.html",
    "size": "M",
    "timer": 20,
    "email": os.getenv('RECEIVER')
}
```
- If the user inputs 2 for No, the program will prompt the user to input the necessary information.
```
Input the url for the item: https://www.zara.com/us/en/plaid-blazer-p02010745.html

        0 : XS
        1 : S
        2 : M
        3 : L
        4 : XL
        5 : XXL
        
Input the size of the item (0 - 5): 2
Input the timer to refresh the item (1 - 60 seconds): 20
Input the email you wish to recieve a notification once the product is in stock (email@gmail.com):email@gmail.com
```
- If the program is able to validate all inputs, then the program will begin to run and it should look like this!
```
Searching for... PLAID BLAZER
The process will continue to refresh every 20 seconds
Press and hold ctrl + c to end the loop
The PLAID BLAZER is out of stock in size: M
```
- The program will continue to run in intervals until the user breaks it or the product is in stock.
```
The Product is in stock
E-mail has been sent Online
```
- Once the product is in stock, the program will use the emailNotifier.py to send an email to the RECEIVER specified in the .env.
- To test your program locally, run the following in a seperate terminal and change the onlineBool to false
```python
#emailNotifier.py
onlineBOOL = False
```
Seperate Terminal Window
```
python -m smtpd -c DebuggingServer -n localhost:1025
```
- If the window catches the email it should look like this
```
---------- MESSAGE FOLLOWS ----------
Subject: Your Product is In-Stock!
X-Peer: 127.0.0.1

Hello!

The product you have been looking for is now in stock.

Follow the link below to go buy it now!

https://www.zara.com/us/en/plaid-blazer-p02010745.html
------------ END MESSAGE ------------
```

## Downloads
- [Python](https://www.python.org/downloads/)
- [Package: python-dotenv](https://pypi.org/project/python-dotenv/)
- [Package: Requests](https://pypi.org/project/requests/)
- [Package: Validators](https://pypi.org/project/validators/)
- [Package: Beautiful Soup](https://pypi.org/project/beautifulsoup4/)

## References
- [How to send email with Python](https://realpython.com/python-send-email/)
- [Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Bypassing 403 error Beautiful Soup](https://www.youtube.com/watch?v=6RfyXcf_vQo)

## Author Info
#### Alexander Shen - Developer
- [LinkedIn](https://www.linkedin.com/in/shenalexw/)
- [Portfolio Website](https://shenalexw.github.io/)

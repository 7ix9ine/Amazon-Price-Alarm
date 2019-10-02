"""
Author: Michele Corlito
Amazon Price Alarm
Automatically sends you an e-Mail when the price of a selected product drops.
"""
from bs4 import BeautifulSoup
import smtplib
import time
import subprocess
import requests

#welcome part
print("Welcome to the amazon python price alarm!")
time.sleep(2)
print("")
sendto = input('please enter your email adress: ')
URL = input("please enter the amazon product url: ")
lower_price = float(input("please enter your wish price(eg.:200, 400, 20, ...): "))
#welcome part

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}

#checks price and if lower than selected lower price send email
def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])

    if(converted_price < lower_price):
        send_mail()

    print(converted_price)
    print(title.strip())

#sends email
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('michelecorlito1@gmail.com', 'xfohcqwupkrmgbjm')

    subject = 'Price dropped!'
    body = 'Check the amazon link: ' + URL

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'michelecorlito1@gmail.com',
        sendto,
        msg
    )
    print("E-Mail has been sent!")

    server.quit
#repeats everything
while(True):
    check_price()
    time.sleep(3600)
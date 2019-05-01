from bs4 import BeautifulSoup
from colorama import Style, Back, Fore
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.parse import quote


def scraper(url):
    answer = []
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html, features="html.parser")
        tmp1 = bsObj.findAll('p', {"class", "day-link"})
        tmp = bsObj.findAll('a', {"class": 'day-link'})
        temp = bsObj.findAll('div', {"class": 'temperature'})
        res = tmp1 + tmp
    except AttributeError as e:
        return print(e)
    for i in range(7):
        answer.append(res[i].get_text() + temp[i].get_text())
    return answer


for day in scraper(
        'https://sinoptik.ua/' + quote("погода-" + input("В каком городе вы хотите узнать погоду?\n"))  ):
    print(Back.LIGHTBLACK_EX)
    print(Fore.GREEN, day)

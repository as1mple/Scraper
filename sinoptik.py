from bs4 import BeautifulSoup
from colorama import Style, Back, Fore
from urllib.request import urlopen
from urllib.error import HTTPError


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
        "https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%B2%D0%B8%D0%BD%D0%BD%D0%B8%D1%86%D0%B0/2019-05-01"
    ):
    print(Back.LIGHTBLACK_EX)
    print(Fore.GREEN, day)

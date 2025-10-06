import requests
from bs4 import BeautifulSoup


def get_main(url):
    response = requests.get(url)
    resp = BeautifulSoup(response.text, 'html.parser')
    fio = resp.find('h1', class_='person-caption').text
    pos = resp.find('span', class_="person-appointment-title").text.strip()[:-1]
    answer = (fio, pos)
    lang = resp.find('dt', class_='b').find_all()
    print(answer)
    long = len('Владение языками')
    print(resp.find('dt', class_='b').text[:long] + ':')
    for i in lang:
        print(i.text)



get_main("https://www.hse.ru/staff/allat")
get_main("https://www.hse.ru/org/persons/135897")
get_main("https://www.hse.ru/org/persons/63890353")
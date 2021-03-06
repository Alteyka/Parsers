import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('Викторины.csv', 'a') as f:       # Создаю файл для дозаписи.
        writer = csv.writer(f)                  # Определяю метод писателя,
        writer.writerow([data['number'],        # который при вызове запишет данные в csv файл
                         data['question'],
                         data['answer']])




def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
# Нахожу нужные теги.
    trs = soup.find_all('tr', {'class': 'tooltip'})
# В каждом trs ищу элементы, записываю в словарь.
# Записываю словарь в csv с помощь функции выше.
    for tr in trs:
        tds = tr.find_all('td')
        number = tds[0].text
        question = tds[1].find('a').text
        answer = tds[2].text

        data = {'number': number,
                'question': question,
                'answer': answer}

        write_csv(data)






def main():
    pattern = 'https://baza-otvetov.ru/categories/view/1/{}'
# В цикле генерирую числа и подставляю каждую итерацию в url
    for i in range(0, 3010, 10):
        url = pattern.format(str(i))
        get_page_data(get_html(url))




if __name__ == '__main__':
    main()


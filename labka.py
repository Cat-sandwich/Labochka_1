from base64 import encode
import requests
import lxml
from bs4 import BeautifulSoup
from time import sleep
import random


def read_url():
    url_film_list = []

    url = 'https://www.kinopoisk.ru/lists/movies/top250/?page=2'
    response = requests.get(url)
    result = response.text
    soup = BeautifulSoup(result, 'lxml')

    # находим все фильмы на странице
    films = soup.find_all('a',  class_='base-movie-main-info_link__YwtP1')

    print(3)

    for film in films:
        url_film = film.get('href')
        url_film_list.append(url_film)

    # сохранение ссылок в файл + сразу поподаем на сайт с рецензией
    with open('url_film_list_2.txt', 'w') as file:
        for line in url_film_list:
            file.write('https://www.kinopoisk.ru' +
                       f'{line}' + 'reviews/ord/rating/status\n')


headers = {
    'User-Agent': 'Mozilla/5.0'
}


def new_txt(status):
    status = status.replace('/', '')
    file = open('url_film_list.txt', 'r')
    lines = file.readlines()
    file.close()
    with open('url_film_list_' + status + '.txt', 'w') as file_2:
        for line in lines:
            line = line.strip()
            line += '/' + status + '/perpage/200\n'
            file_2.write(line)


def print_lines(status):
    file = open('url_film_list_2_' + status + '.txt', 'r')
    lines = file.readlines()
    file.close()
    j = 929

    while (j != 1000):
        for line in lines:
            line = line.strip()

            response = requests.get(line, headers=headers)
            print("#"*100)
            print(response.text)
            print("#"*100)
            result = response.content
            soup = BeautifulSoup(result, 'lxml')
            sleep(random.randint(60, 66))

            try:
                reviews = soup.find_all(class_='_reachbanner_')
            except AttributeError as e:
                print("Не найдена рецензия!!!")
                
                sleep(30)
                continue
            for review in reviews:
                if j < 10:
                    with open('dataset/' + status + '/000' + str(j) + '.txt', 'a', encoding='utf-8') as file:
                        name = soup.find(class_='breadcrumbs__link')
                        text = name.text.strip()
                        file.write(text + '\n')
                        file.write(soup.find(class_='sub_title').text)
                        text_reviews = review.text.strip()
                        file.write(text_reviews)
                        print('_________DOWNLOAD FILE №', j, '___________')
                if j >= 10 and j < 100:
                    with open('dataset/'  + status + '/00' + str(j) + '.txt', 'a', encoding='utf-8') as file:
                        name = soup.find(class_='breadcrumbs__link')
                        text = name.text.strip()
                        file.write(text + '\n')
                        file.write(soup.find(class_='sub_title').text)
                        text_reviews = review.text.strip()
                        file.write(text_reviews)
                        print('_________DOWNLOAD FILE №', j, '___________')
                if j >= 100 and j < 1001:
                    with open('dataset/' + status + '/0' + str(j) + '.txt', 'a', encoding='utf-8') as file:
                        name = soup.find(class_='breadcrumbs__link')
                        text = name.text.strip()
                        file.write(text + '\n')
                        file.write(soup.find(class_='sub_title').text)
                        text_reviews = review.text.strip()
                        file.write(text_reviews)
                        print('_________DOWNLOAD FILE №', j, '___________')
                j += 1
                if j == 1000:
                    break


status = 'bad'

#new_txt(status)
status = 'good'
#new_txt(status)
#print_lines(status)
status = 'bad'
print_lines(status)

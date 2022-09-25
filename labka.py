import requests
import lxml
from bs4 import BeautifulSoup
from time import sleep
def read_url():
    url_film_list = []

    url = 'https://www.kinopoisk.ru/lists/movies/top250/'
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
    with open('url_film_list.txt', 'w') as file:
        for line in url_film_list:
            file.write('https://www.kinopoisk.ru' + f'{line}' + 'reviews/ord/rating/status\n')

status = '/bad/'

    
def print_lines(status):
        file = open('url_film_list.txt', 'r')
        lines = file.readlines() 
        file.close
        for line in lines:
            line = line.strip() 
            
            line +=  status + 'perpage/10/page/1'
            response = requests.get(line)
            result = response.text
            soup = BeautifulSoup(result, 'lxml')
            
            sleep(5)
            print(soup)
            count = soup.find(class_="pagesFromTo").text
            count = count.split(' ')
            print(count[2])
            page = count[2]
            num_page = int(page)//10
            if int(page)%10 > 0:
                num_page +=1
            i=1
            for i in num_page:
                url_reviews = line[:-1] + i
                response = requests.get(line)
                result = response.text
                soup = BeautifulSoup(result, 'lxml')
                j = 0
                with open('dataset/' + status + '/' + j +'.txt', 'w') as file:
                    file.write(soup.find(class_='breadcrumbs__link').text)
                    file.write(soup.find(class_='sub_title').text)
                    reviews = soup.find_all(class_='_reachbanner_')
                    for review in reviews:
                        file.write(review.text)

              


     
                
print_lines(status)

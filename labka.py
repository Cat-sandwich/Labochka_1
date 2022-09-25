import requests
import lxml
from bs4 import BeautifulSoup

url_film_list = []

url='https://www.kinopoisk.ru/lists/movies/top250/'
response = requests.get(url)
result = response.text
soup = BeautifulSoup(result, 'lxml')


films = soup.find_all('a',  class_='base-movie-main-info_link__YwtP1') #находим все фильмы на странице

print(3)

for film in films:
    url_film = film.get('href')
    url_film_list.append(url_film)
    
with open('url_film_list.txt', 'w') as file: # сохранение ссылок в файл
    for line in url_film_list:
        file.write( 'https://www.kinopoisk.ru' + f'{line}' + 'reviews/\n')

def function ():
   with open('url_film_list.txt', 'w') as file:
    file.readline() 

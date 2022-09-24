import requests
import lxml
from bs4 import BeautifulSoup

url_film_list = []

url='https://www.kinopoisk.ru/lists/movies/top250/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')


films = soup.find_all( 'a', class_='base-movie-main-info_link__YwtP1') #находим все фильмы на странице base-movie-main-info_link__YwtP1  styles_main__Y8zDm styles_mainWithNotCollapsedBeforeSlot__x4cWo
print(films)
print(3)

for film in films:
    url_film = film.get('href')
    url_film_list.append(url_film)
    
with open('url_film_list.txt', 'a') as file:
    for line in url_film_list:
        file.write(f'{line}\n')

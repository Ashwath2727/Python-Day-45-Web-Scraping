import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

movies = [movie.getText() for movie in soup.find_all(name="h3", class_="title")]
movies.reverse()
print(movies)

with open("top_100_movies.txt", "w") as file:
    for movie in movies:
        file.write(f"{movie.replace("â\x80\x93", "-")}\n")
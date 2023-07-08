from bs4 import BeautifulSoup
import requests

repsonse = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
my_file = repsonse.text

soup = BeautifulSoup(my_file, "html.parser")


def my_css(css_class):
    return (
        css_class is not None
        and "https://www.empireonline.com/movies/reviews" in css_class
    )


my_anchor = soup.find_all(href=my_css)
print(my_anchor)

a = 1
with open("100 Movies/Movies.txt", mode="w") as file:
    file.write(" Top 100 movies\n")
    for tag in my_anchor:
        movie_name = ""
        my_list = tag.text.split()
        if len(my_list) > 2:
            for i in range(4, len(my_list)):
                movie_name = movie_name + " " + my_list[i]
        else:
            continue

        file.write(f"{a}) {movie_name}\n")
        a += 1

# memrise scraper
from bs4 import BeautifulSoup
import requests
import lxml

BASE_URL = "https://app.memrise.com"
FILENAME = "FILENAME.csv"

# JLPT N5 - https://app.memrise.com/course/554/jlpt-n5-vocab/
# JLPT N4 - https://app.memrise.com/course/122925/jlpt-n4-readings/
# JLPT N3 - https://app.memrise.com/course/1584135/jlpt-n3-readings-with-audio/
# JLPT N2 - https://app.memrise.com/course/24151/jlpt-n2-from-memrise-beta/

search = "INSERT-COURSE-HERE"
r = requests.get(search)
xml = BeautifulSoup(r.content, "lxml")
levels = xml.find_all("a", {"class": "level clearfix"})
levels = levels[1:]

with open(FILENAME, "w") as file:
    for level in levels:
        level = BASE_URL + level["href"]
        level_r = requests.get(level)
        level_xml = BeautifulSoup(level_r.content, "lxml")
        words_html = level_xml.find_all("div", {"class": "things clearfix"})
        words = words[0].find_all("div", {"class": "text"})
        
        counter = 1
        for word in words:
            if counter % 2 == 0:
                counter = 1
                continue
            file.write(f"{word.text},")
            counter += 1
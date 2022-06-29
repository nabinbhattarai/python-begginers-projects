import requests
from bs4 import BeautifulSoup as bs
url = "https://data-flair.training/blogs/django-sessions/"
result = requests.get(url)
doc = bs(result.text,"html.parser")
tag = doc.find_all(["p"])  #extracting data of specific tags
tags = doc.find_all(["input"])
print(tag)
print(tags)

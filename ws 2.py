from bs4 import BeautifulSoup
import requests

search = input('enter search term :')
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text)
print(soup.prettify())
results = soup.find("ol", {"id": "b_result"})
links = results.find_all("li", {"class", "b_algo"})

for items in links:
    items_text = items.find("a").text
    items_href = items.find("a").attrs["href"]

    if items_text and items_href:
        print(items_href)
        print(items_text)

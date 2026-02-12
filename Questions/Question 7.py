import requests
from bs4 import BeautifulSoup
# wikipedia doesnt allow scraping without a user-agent header, heres mine:
myUserAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0"
}

dataScienceHTML = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=myUserAgent).text

# turn it into a soup element
dataScienceHTMLSoup = BeautifulSoup(dataScienceHTML, "html.parser")

# take the text of the title element
dataScienceHTMLTitle = dataScienceHTMLSoup.find("title").get_text()

print(dataScienceHTMLTitle)

# its an id so theres only one div with this attribute
dataScienceHTMLDiv = dataScienceHTMLSoup.find(id="mw-content-text")


dataScienceHTMLP = dataScienceHTMLDiv.find_all("p")

# find the second p element, the very first one is "empty"
print(dataScienceHTMLP[1].get_text())

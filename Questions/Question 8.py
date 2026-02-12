import requests
from bs4 import BeautifulSoup
# wikipedia doesnt allow scraping without a user-agent header, heres mine:
myUserAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0"
}
dataScienceHTML = requests.get("https://en.wikipedia.org/wiki/Data_science", headers=myUserAgent).text

# turn it into a soup object
dataScienceHTMLSoup = BeautifulSoup(dataScienceHTML, "html.parser")

# similar process to question 7
dataScienceHTMLDiv = dataScienceHTMLSoup.find(id="mw-content-text")
dataScienceHTMLHeadings = dataScienceHTMLDiv.find_all("h2")
avoidList = ["See also", "References", "External links", "Notes"]

# the first table with more than 3 rows has only one columns
headingsFile = open("../Program-Created Files/headings.txt", mode="w")
for h2 in dataScienceHTMLHeadings:
    h2Text = h2.get_text()
    if h2Text not in avoidList:
        print(h2Text)
        headingsFile.write(h2Text+"\n")

headingsFile.close()

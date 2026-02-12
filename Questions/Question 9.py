import requests
import csv
from bs4 import BeautifulSoup

myUserAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:148.0) Gecko/20100101 Firefox/148.0"
}
machineLearningHTML = requests.get("https://en.wikipedia.org/wiki/Machine_learning", headers=myUserAgent).text

# similar process to last 2 questions
machineLearningHTMLSoup = BeautifulSoup(machineLearningHTML, "html.parser")

machineLearningHTMLDiv = machineLearningHTMLSoup.find(id="mw-content-text")
machineLearningHTMLTable = machineLearningHTMLDiv.find("table")

machineLearningHTMLTableTr = machineLearningHTMLTable.find_all("tr")

with open("../Program-Created Files/wiki_table.csv", "w", newline="") as csvfile:
    wikiTableWriter = csv.writer(csvfile)
    for tr in machineLearningHTMLTableTr:
        string = tr.get_text()
        wikiTableWriter.writerow(string.split())



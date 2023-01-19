import requests, os, openai
# my_secret = os.environ['openai']
# my_secret = os.environ['organisationID']
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Hair_loss"

response = requests.get(url)
html = response.text

# print(html)

soup = BeautifulSoup(html, 'html.parser')
# div
# mw-parser-output
# p

article = soup.find_all("div", {"class": "mw-parser-output"})[1]
# for section in article:

content = article.find_all("p")
# content = soup.find_all("p")

print(len(content))

text = ""
for p in content:
  text += p.text

# print(text)
openai.organisation = os.environ['organisationID']
openai.api_key = os.environ['openai']
openai.Model.list

refs = soup.find_all("ol", {"class": "references"})
for ref in refs:
  print(ref.text.replace("^", ""))

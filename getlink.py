from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json

url = "https://imginn.com/search/?q=sexy+girl"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a.tab-item")
l = []
for link in links:
    a = link["href"].replace('/', '')
    l.append(f"https://imginn.com/{a}")

data = {
    "links": l,
}
with open('links.json', 'w') as fp:
    json.dump(data, fp)
driver.close()

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

url = "https://imginn.com/search/?q=hot+girl"
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
time.sleep(1)


html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
links = soup.select("a.tab-item")

print("[")
for link in links:
    a = link["href"].replace('/', '')
    print(f'"https://imginn.com/{a}",')
print("]")

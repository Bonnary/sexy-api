from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import json


def scrape(URL):

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(URL)

    # wait for browser to load
    time.sleep(1)

    # scroll to bottom page 30 times every 3 seconds
    for i in range(20):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    images_container = soup.select("div.item img")

    # open old data source
    with open('data.json') as f:
        data_old = json.load(f)

    data = {}
    i = len(data_old) + 1

    # scraping data
    for image in images_container:
        if (image['src'] != "//s1.imginn.com/img/lazy.jpg"):
            username = soup.select_one('div.username').text.replace(
                '(', '').replace(')', '')
            data[i] = {"username": username, "image": image["src"]}
            i += 1

    # update old data with new data
    data_old.update(data)

    # write it to json file
    with open('data.json', 'w') as fp:
        json.dump(data_old, fp)
    driver.close()


links_data = json.load(open('links.json', 'r'))
urls = links_data["links"]


for url in urls:
    scrape(url)

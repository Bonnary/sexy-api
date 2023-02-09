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
    for i in range(30):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

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


urls = [
    "https://imginn.com/sexy_video_girl12",
    "https://imginn.com/hot_sexi_videos",
    "https://imginn.com/hot_girls_movie",
    "https://imginn.com/girl_hot_video_0808",
    "https://imginn.com/sexy_hot796",
    "https://imginn.com/miya_kalifa_hot",
    "https://imginn.com/dating.usa.girls",
    "https://imginn.com/hotgirlmakeout",
    "https://imginn.com/h.s.girls__",
    "https://imginn.com/hot_sexy_girls_pic_and_video_",
    "https://imginn.com/hot_girl_anime__",
    "https://imginn.com/indian_sexy_figure",
    "https://imginn.com/hotty_indiangirl",
    "https://imginn.com/indian_hot_girl____",
    "https://imginn.com/hot_chinese_girl_099",
    "https://imginn.com/hot_girls_fotos_",
    "https://imginn.com/hot_anime_girlls",
    "https://imginn.com/hotg.irl81581",
    "https://imginn.com/hot.mayara",
    "https://imginn.com/_hot_and_sexy_anime_girls_",
    "https://imginn.com/hotgirlinsaree",
    "https://imginn.com/massgaeserviceindohaqatar",
    "https://imginn.com/naked_top_models",
    "https://imginn.com/hot.girls_69",
    "https://imginn.com/perverso.a1",
    "https://imginn.com/sexy_hot_desi_girl",
    "https://imginn.com/blondebabe.s",
    "https://imginn.com/_hot_boy_124568",
    "https://imginn.com/world_best_girl",
    "https://imginn.com/vietnams3xygirl",
    "https://imginn.com/hot_and_sexy_girls_bhabhi",
    "https://imginn.com/classic.divaz",
    "https://imginn.com/gbg_inst",
    "https://imginn.com/sexy_babe_.____",
    "https://imginn.com/teens.babes",
    "https://imginn.com/curvy.hotgirls",
    "https://imginn.com/anime_nude14748",
    "https://imginn.com/ifoundthehotgirl",
    "https://imginn.com/hot_and_cute_asian_girl",
    "https://imginn.com/hot_girls_pics_x69",
    "https://imginn.com/hot_sexy_girls_pic_and_videos",
    "https://imginn.com/hot_girls_shoot1",
    "https://imginn.com/hot_korean_girls_",
]


for url in urls:
    scrape(url)

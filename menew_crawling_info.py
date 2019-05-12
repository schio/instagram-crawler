from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import driver
import json
import requests

def getFoodImgAtInstagram(hashtag):
    # 인스타그램 공식 홈페이지
    instagramHompage = 'https://www.instagram.com'
    url = 'https://www.instagram.com/explore/tags/'+hashtag

    # 크롬 드라이버 생성
    browser = driver.createDriver(url)
    time.sleep(1.5) # URL 접속 후 모든 정보 불러오기 위한 1초 대기시간 부여

    elem = browser.find_element_by_tag_name("body")

    elem.send_keys(Keys.PAGE_DOWN)
    elem.send_keys(Keys.PAGE_DOWN)

    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    select_imgs = soup.select('main > article > div.EZdmt > div > div > div > div > a > div > div > img')

    print(len(select_imgs))
    print(type(select_imgs))

    food_img_urls = []
    for select_img in select_imgs:
        src_url = select_img['src']
        food_img_urls.append(src_url)

    # f = open("links__.txt", 'w')
    # for url in food_img_urls:
    #     temp = url+'\n'
    #     f.write(temp)
    # f.close()

    meta = {
        'urls' : food_img_urls # 사진 url
    }
    # print(meta)
    return json.dumps(meta, ensure_ascii=False)

# def getFoodImgAtGoogle(name):
#     url = 
start_time = time.time()
# getFoodImgAtInstagram('김치볶음밥')
print(time.time() - start_time)

# https://www.google.com/search?q=tapas&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjf8Jnl7pPiAhVJL6YKHSKvCDAQ_AUIDigB&biw=819&bih=918&dpr=2
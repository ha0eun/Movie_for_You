# 리뷰 크롤링 -> 리뷰를 보고 비슷한 리뷰의 영화를 추천

from selenium import webdriver      # pip install selenium==4.6.0
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)

url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open=2022&page=1'













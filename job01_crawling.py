# crawling 컬럼명 ['titles', 'reviews]  로 통일해주세요
# 파일명은  'reviews_{}.csv'.format(연도)  로 해주세요

# 리뷰 크롤링 -> 리뷰를 보고 비슷한 리뷰의 영화를 추천
from selenium import webdriver      # pip install selenium==4.6.0
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()

options.add_argument('lang=ko_KR')
driver = webdriver.Chrome('./chromedriver.exe', options=options)

review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a' # 동영상 있음/ 리뷰탭
review_num_path = '//*[@id="reviewTab"]/div/div/div[2]/span/em' # 총 리뷰 수
review_xpath = '//*[@id="content"]/div[1]/div[4]/div[1]/div[4]' # 리뷰

# '//*[@id="old_content"]/ul/li[1]/a'
# '//*[@id="old_content"]/ul/li[20]/a'

your_year = 2017   # 2016, 2017
for page in range(1, 54):      # 1페이지 - 까지 60, 54
    url = 'https://movie.naver.com/movie/sdb/browsing/bmovie.naver?open={}&page={}'.format(your_year, page)
    titles = []
    reviews = []

    try:
        for title_num in range(1, 21):
            driver.get(url)
            time.sleep(0.1)

            movie_title_xpath = '//*[@id="old_content"]/ul/li[{}]/a'.format(title_num)  # 영화제목
            title = driver.find_element('xpath', movie_title_xpath).text
            print('title', title)
            driver.find_element('xpath', movie_title_xpath).click()
            time.sleep(0.1)
            try:
                # review_button_xpath = '//*[@id="movieEndTabMenu"]/li[6]/a' # 증복되서 for문 밖으로 뺌/ 동영상 있음/ 리뷰탭
                driver.find_element('xpath', review_button_xpath).click()
                time.sleep(0.1)

                # review_num_path = '//*[@id="reviewTab"]/div/div/div[2]/span/em' 증복되서 for문 밖으로 뺌
                review_num = driver.find_element('xpath', review_num_path).text
                review_num = review_num.replace(',', '')    # 기생충 같은 영화는 리뷰가 많아서 1000개가 넘기때문에 1000단위에 ‘ , ‘가 생기기때문에 없애줘야함
                review_range = (int(review_num) -1)  // 10 + 1  # 한페이지에 10개가 있으면 10/10=0이라서
                # 페이지가 2페이지가 나온다고 되니까 -1을 먼저하고 9를 나눠서 몫에 +1 하면 페이지 정확하게 구할 수 있음

                if review_range > 3:    # 리뷰페이지는 3페이지까지만 확인하자
                    review_range = 3

                for review_page in range(1, review_range +1):   # 리뷰 페이지
                    review_page_button_xpath = '//*[@id="pagerTagAnchor{}"]'.format(review_page)
                    driver.find_element('xpath', review_page_button_xpath).click()
                    time.sleep(0.1)

                    for review_title_num in range(1, 11):
                        review_title_xpath = '//*[@id="reviewTab"]/div/div/ul/li[{}]/a'.format(review_title_num)
                        driver.find_element('xpath', review_title_xpath).click()    # 리뷰 제목 긁기
                        time.sleep(0.1)
                        try:
                            # review_xpath = '//*[@id="content"]/div[1]/div[4]/div[1]/div[4]'  #증복되서 for문 밖으로 뺌/ 리뷰
                            review = driver.find_element('xpath', review_xpath).text
                            titles.append(title)
                            reviews.append(review)
                            driver.back()       # 리뷰 읽고 뒤로 가기(다른 리뷰 보려고)
                        except:
                            print('review', page, title_num, review_title_num)
                            driver.back()
            except:
                print('review button', page, title_num)
            # for문 다돌고 빠져나왔을때
        df = pd.DataFrame({'titles':titles, 'reviews':reviews})
        df.to_csv('./crawling_data/reviews_{}_{}page.csv'.format(your_year, page), index=False) #index=False 인덱스 필요없음
    except:
        print('error', page, title_num)



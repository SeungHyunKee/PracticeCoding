from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Pool   # 동시에 여러개 창 뜨게 
import time
import os
import urllib.request
import pandas as pd  # 텍스트파일을 읽어오기 위함

'''
폴더 구성
'''
def create_folder(directory):
    try:  # 폴더생성
        if not os.path.exists(directory):
            os.makedirs(directory)

    except OSError:
        print('error : Creating directory...' + directory)
# 디렉토리가 있는경우에만 생성하고, 없으면 넘어가




# 검색 키워드 호출
key = pd.read_csv('./keyword.txt', encoding='utf-8', names=['keyword'])
# read_csv 로 .있는 데이터 읽어올수 있다  / window : encoding = 'cp949' ?
keyword = []  # 키워드 저장
[keyword.append(key['keyword'][x]) for x in range(len(key))]
print(keyword)




def image_download(keywords):
    create_folder("./" + keywords + "_low_resolution")

    # 크롬 드라이브 호출
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    chromedriver = "./chromedriver.exe"
    chromedriver.exe
    driver = webdriver.Chrome(chromedriver, options=options)
    driver.implicitly_wait(3)


      # 검색
    print('검색 >> ', keywords)
    driver.get("https://www.google.co.kr/imghp?h1=ko") # 사이트를 실행
    keyword = driver.find_element_by_xpath(            # inout창에 커서가 가게됨
        '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    keyword.send_keys(keywords)                        # 해당 키워드로 창이 뜨게됨
    keyword.send_keys(Keys.RETURN)


# #  ========================
# # 실행
# # =========================
# if __name__ == '__main__':
#     pool = Pool(processes=3)
#     pool.map(image_download, keyword)


    # 스크롤 내리기 -> 결과 더보기 버튼 클릭
print("스크롤 ..... ", keywords)
elem = driver.find_element_by_tag_name('body')
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)  # 스크롤이 너무 빨리 내려가면 웹사이트에 차단이 걸리게 되므로 sleep값 설정

try:
    # //*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input  이값은 내가 직접 찾아오기
    driver.find_element_by_xpath(
        '//*[@id="islmp"]/div/div/div/div[2]/div[1]/div[2]/div[2]/input').click()
    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
except:
    pass  # 에러있으면 패스해라


    links = []
    images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")
    for image in images:
        if image.get_attribute('src') != None:
            links.append(image.get_attribute('src'))

    print(keywords + '찾은 이미지 개수 : ', + len(links))
    time.sleep(2)

    for index, i in enumerate(links):
        url = i
        start = time.time()   # 다운로드 걸린시간 알려줌
        urllib.request.urlretrieve(
            url, "./" + keywords + "_low_resolution/" + keywords + "_" + str(index) + ".jpg")
        print(str(index+1) + "/" + str(len(links)) + " " + keywords +
              " 다운로드 시간 ------ : ", str(time.time() - start)[:5] + '초')
    print("다운로드 완료 !!!!")


if __name__ == '__main__':
    pool = Pool(processes=3)
    pool.map(image_download, keyword)
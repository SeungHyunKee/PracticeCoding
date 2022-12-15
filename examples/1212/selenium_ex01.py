from selenium import webdriver # 웹드라이버 호출

from selenium.webdriver.common.keys import Keys  # Keys 대문자 주
import time  # 이미지 다운로드 시간 보여줄 time
import os  # 경로와 관련
import urllib.request  # selenium통해 가져온 이미지들의 url 불러들여 이미지 저장하게함

'''
폴더 구성
'''
def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

    except OSError:
        print('error : Creating directory...' + directory)
# 디렉토리가 있는경우에만 생성하고, 없으면 넘어가


"""
키워드 입력 , chromedriver 실행
"""
# option값 추가하면 열린 창 안꺼지게 해줌 (버전 1.8 이하)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

keywords = "사과"  # 내가 검색할 검색어
chromedriver_path = "./chromedriver.exe"  # 윈도우라면 ./chromedriver 뒤에 .exe붙이기


driver = webdriver.Chrome(chromedriver_path, options=options)
driver.implicitly_wait(3)  # 대기시간 

#####
# 키워드 입력 selenium 실행
#####
driver.get("https://www.google.co.kr/imghp?h1=ko")   # 구글 검색창 띄우기

### find_element_by_path 이용하는 방법 (XPATH : XML Path Language) ###
''' 개발자도구로 검색창 코드 복사해온
<input class="gLFyf" jsaction="paste:puy29d;" maxlength="2048" name="q" type="text" 
aria-autocomplete="both" aria-haspopup="false" autocapitalize="off" autocomplete="off"
autocorrect="off" autofocus="" role="combobox" spellcheck="false" title="검색" value=""
aria-label="검색" data-ved="0ahUKEwiYl8mCxvT7AhVrx4sBHbbUCbEQ39UDCAY">
'''
# 개발자도구에서 검색창부분에서 copy - xpath 복사
# input -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input
# 검색창옆 버튼의 xpath
# button -> /html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button

keyword = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
keyword.send_keys(keywords)
keyword.send_keys(Keys.RETURN)
# driver.find_element_by_xpath(
#     '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button').click()

### find_element_by_name 이용하는 방법 ###
# elem = driver.find_element_by_name("q")  # 검색창으로 마우스 커서가 움직이게 됨
# elem.send_keys(keyword)  # 입력창에 키워드가 입력이 됨
# elem.send_keys(Keys.RETURN)  # 리턴을 주게되면 버튼을 누른것처럼 된다

# <input class = "gLFyf" jsaction = "paste:puy29d;"
# maxlength = "2048" name = "q" type = "text" aria-autocomplete = "both"
# aria-haspopup = "false" autocapitalize = "off" autocomplete = "off"
# autocorrect = "off" autofocus = "" role = "combobox"
# spellcheck = "false" title = "검색" value = ""
# aria-label = "검색" data-ved = "0ahUKEwjK5OHq__L7AhVeQPUHHZemCioQ39UDCAM" >



######### 스크롤 ##########
# 스크롤 자동으로 내리기
print(keywords + '스크롤 중 .......')
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
    pass

links = []
images = driver.find_elements_by_css_selector("img.rg_i.Q4LuWd")  # 이 클래스 id는 동일

for image in images:  # 이미지 하나씩 꺼내오기
    if image.get_attribute('src') != None:  # image src = 'base64'
        links.append(image.get_attribute('src'))

print(keywords + "찾은 이미지 개수 : ", len(links))
print(links)
time.sleep(2)


""" 데이터 다운로드 
link 에 들어있는 link를 urllib.request를 통해 하나씩 요청하고, 해당이미지들을
'키워드_number' 형태로 위에서 만들어준 폴더에 저장한다
"""
create_folder('./'+keywords+'_img_download')
for index, i in enumerate(links):  ## enumerate 를 이용하기때문에 count +1 식으로 안해줘도됨
    url = i
    start = time.time()
    urllib.request.urlretrieve(
        url, "./" + keywords + "_img__download/" + keywords + "_" + str(index) + ".jpg")
    print(str(index) + "/" + str(len(links)) + " " + keywords +
          " 다운로드 시간 ------ : ", str(time.time() - start)[:5] + '초')

print(keywords + "다운로드 완료 !!")
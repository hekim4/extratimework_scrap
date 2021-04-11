#00님이 문의하신 수작업 자동화

import urllib.request 
import urllib.parse 
from bs4 import BeautifulSoup 

sth_list = []
pageNum = 1

#이하는 1페이지 테스트 코드 : 파싱한 정보중에서 원하는 정보(청구기호, 이미지버튼 O/X, 텍스트버튼 O/X)만 추출하기 작업중
url = 'http://kyudb.snu.ac.kr/book/list.do?pageIndex=10'
html = urllib.request.urlopen(url).read() 

soup = BeautifulSoup(html, 'html.parser') 

bcode = soup.select('ul > li > dl > dd > p > span')
bbtn = soup.select('ul > li > div')

#print(bcode)
#print(type(bbtn))
#print(len(bbtn))
#tmp = bbtn
#print(type(tmp))

"""
#print(bbtn[96]) #https://tariat.tistory.com/525 이거보고 뷰티플숩 자체를 공부하는게 필요
print(str(soup.find_all("span")[29])[12:-7])
print(str(soup.find_all("span")[35])[12:-7]) #이거 append하면됨 ㅋ
print(soup.find_all("span")[41])
print(soup.find_all("span")[47]) #20개 리스트 청구기호: 29, 35, 41, 47, , ,  번째 (+6)
print(soup.find_all("span")[53])
print(soup.find_all("span")[59])
print(soup.find_all("span")[65])
print(soup.find_all("span")[71])
print(soup.find_all("span")[77])
print(soup.find_all("span")[83]) 
print(soup.find_all("span")[89])
print(soup.find_all("span")[95])
print(soup.find_all("span")[101])
print(soup.find_all("span")[107])
print(soup.find_all("span")[113])
print(soup.find_all("span")[119])
print(soup.find_all("span")[125])
print(soup.find_all("span")[131])
print(soup.find_all("span")[137])
print(soup.find_all("span")[143])
print(soup.find_all("span")[149])
"""
print(soup.find_all("/images/old/btn_img.png")) #통으로 문자화시키고 이미지 아이콘 네임값 검색한담에 위치찾기?? 코드매칭??


#여기까지 테스트 코드


#이하는 실제 버전
"""
while pageNum < 2170:
    url = f'http://kyudb.snu.ac.kr/book/list.do?pageIndex={pageNum}'  #페이지 넘김 절대주소는 자바스크립트 콘솔 켜고 돔 뜯어보면 됨. 로딩되는 코드를 잘 봐야 (http://kyudb.snu.ac.kr/book/list.do?pageIndex=9)
    html = urllib.request.urlopen(url).read() 

    soup = BeautifulSoup(html, 'html.parser') 

    #bname = soup.select('#panel > div.panel_content.nano.has-scrollbar > div.scroll_pane.content > div.panel_content_flexible > div.search_result > ul > li > div.lsnx > dl > dt > a')
    bcode = soup.select('ul > li > dl > dd > p > span')
    bbtn = soup.select('ul > li > div')


#print(soup)

#with open("test.html", "w") as f:
#    f.write(soup.readlines())

"""
#여기까지 실제 버전






#참조한 코드(아래) 출처 : https://moondol-ai.tistory.com/107
"""
import urllib.request 
import urllib.parse from bs4 
import BeautifulSoup 

post_list = [] 
pageNum = 2 # 슬랙의 경우, 첫 페이지 구조가 달라서 첫 페이지는 따로 긁었습니다. 

while pageNum < 47: 
    # 해당 부분은 블로그마다 다릅니다. 
    url = f'https://slackhq.com/categories/collaboration/page/{pageNum}' 
    html = urllib.request.urlopen(url).read() 
    soup = BeautifulSoup(html, 'html.parser') 
    
    titles = soup.select('header > h3 > a') 
    
    for title in titles: 
        post_list.append([title.text, title.get('href')]) 
        
    pageNum += 1 
    
post_infos = pd.DataFrame(post_list, columns=['title', 'url']) 
post_infos.to_csv('post_infos(slack).csv', encoding='utf-8-sig')
"""
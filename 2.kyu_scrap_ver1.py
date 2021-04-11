"""
업무 편의를 위해 임시로 개발한 프로그램 입니다.
스크래핑 거부 사이트에 대한 스크래핑 행위 및 영리목적의 데이터 무단사용은 문제가 될 수 있는 점을 사전 고지합니다.

$ Kyu_scrap_ver0.py
작성자 : hekim
작성기록 : 2021-03-14 (ver.0)
          2021-03-?? (ver.1 - 서지, 한국어서지 추출코드 추가 및 제작되는 파일에 페이지넘버도 추가)
          *피드백: 성능(스크래핑 속도)에 대해서는 추후 여유시 개선하고 기능개선/정확도 탐색 작업에 더 촛점을 두기로 함

! 경고 : 인터넷이 불안정한 경우 강제 중단될 위험이 있음(중단되기 전까지 읽은 데이터는 저장됩니다)
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup 
import urllib.request, csv, datetime, os

pageNum = int(input("작업을 시작할 페이지 입력(숫자만 입력): "))
end_pNum = int(input("작업을 종료할 페이지 입력(숫자만 입력): ")) #2170

print("\n작업 시작 시간: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),"\n")

print("스크래핑을 시작합니다. . . ({}-{} 페이지)".format(pageNum, end_pNum))
print("※주의 : 데이터 기록 도중 텍스트 파일을 열어보는 것을 권장하지 않습니다.\n")
time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")

with open("kyu_web_scrap_{}({}-{}p).txt".format(time_stamp, pageNum, end_pNum), "a", encoding='UTF-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["URL_ID","서지","서지(KOR)","청구기호","이미지","원문","목차", "소속 페이지", "*이미지/원문/목차 구축 안됨 = -1, 양수는 구축됨을 의미(양수의 값은 의미 없습니다)"])

    while 1:
        print("{}번째 페이지 작업중. . .".format(pageNum))
        
        url = f'http://kyudb.snu.ac.kr/book/list.do?pageIndex={pageNum}'
        html = urllib.request.urlopen(url).read() 
        soup = BeautifulSoup(html, 'html.parser')

        for i in range(1, 21):
            tmp = "#searchResultView_1 > div > ul > li:nth-child({})".format(i)
            tmp_data = str(soup.select(tmp))

            id, idx_s, idx_e, idx_bname, idx_korname = tmp_data.find("value"), tmp_data.find("청구기호"), tmp_data.find("편저자"), tmp_data.find("strong onclick"), tmp_data.find("span onclick")
            idx_bname_end, idx_korname_end = tmp_data.find("</strong>"), tmp_data.find("</span>")

            if tmp_data[id+7:id+17] == "":
                    break
            else:    
                writer.writerow([tmp_data[id+7:id+17], tmp_data[idx_bname+132:idx_bname_end].strip(), tmp_data[idx_korname+102:idx_korname_end].strip(), tmp_data[idx_s+6:idx_e-15], tmp_data.find("old/btn_img"), tmp_data.find("old/btn_txt"), tmp_data.find("old/btn_toc"), pageNum])

        pageNum += 1
        if pageNum == end_pNum+1:
            break

print("작업이 완료되었습니다.\n")
print("작업 종료 시간: ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "\n")

print("※ Tip: 작성 완료된 텍스트 파일을 열어 ctrl+A로\n      전체 선택 및 복사 후 엑셀을 열어 붙여넣고,\n      데이터>텍스트 나누기에서 쉼표(,)로 나눌 시,\n      엑셀에서 작업이 가능합니다!\n")

os.system("pause")
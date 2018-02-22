# Day_02_03_kma.py

import requests
import re

url = 'http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108'
recvd = requests.get(url)
print(recvd)    # <Response [200]>
#print(recvd.text)

tmp = re.findall(r'<province>서울ㆍ인천ㆍ경기도</province>', recvd.text)
#print(tmp)  # ['<province>서울ㆍ인천ㆍ경기도</province>', '<province>서울ㆍ인천ㆍ경기도</province>', '<province>서울ㆍ인천ㆍ경기도</province>', '<province>서울ㆍ인천ㆍ경기도</province>']
print(len(tmp)) # 4

prov = re.findall(r'<province>.+</province>', recvd.text)
#print(prov) # ['<province>서울ㆍ인천ㆍ경기도</province>', '<province>서울ㆍ인천ㆍ경기도</province>', '<province>서울ㆍ인천ㆍ경기도</province>', '<province>서울ㆍ인천ㆍ경기도</province>', '<province>강원도영서</province>', '<province>강원도영서</province>', '<province>강원도영동</province>', '<province>대전ㆍ세종ㆍ충청남도</province>', '<province>대전ㆍ세종ㆍ충청남도</province>', '<province>대전ㆍ세종ㆍ충청남도</province>', '<province>충청북도</province>', '<province>광주ㆍ전라남도</province>', '<province>광주ㆍ전라남도</province>', '<province>광주ㆍ전라남도</province>', '<province>전라북도</province>', '<province>전라북도</province>', '<province>부산ㆍ울산ㆍ경상남도</province>', '<province>부산ㆍ울산ㆍ경상남도</province>', '<province>부산ㆍ울산ㆍ경상남도</province>', '<province>대구ㆍ경상북도</province>', '<province>대구ㆍ경상북도</province>', '<province>대구ㆍ경상북도</province>', '<province>제주도</province>', '<province>제주도</province>']
print(len(prov))    # 24


# 문제
# 전체 location 가져오기

locations = re.findall(r'<location wl_ver="3">.+?</location>', recvd.text, re.DOTALL)
print(len(locations))

def printLoc():
    for loc in locations:
        print(loc)


# 문제
# province 를 찾아서 출력

def printProvince():
    for loc in locations:
        prov = re.findall(r'<province>.+</province>', loc)
        print(prov)


def printProvinceData():
    for loc in locations:
        prov = re.findall(r'<province>(.+)</province>', loc)
        print(prov)


# printProvince()


# Data 찾기

def findData():
    for loc in locations:
        prov = re.findall(r'<province>(.+)</province>', loc)
        city = re.findall(r'<city>(.+)</city>', loc)
        data = re.findall(r'<data>(.+)</data>', loc, re.DOTALL)

        #print(prov[0], prov)
        #print(city[0])
        # print(data)
        # print(len(data))    # 1

        for datum in data:
            # print(datum)

            # 문제
            # mode 를 비롯한 나머지를 찾아보기
            mode = re.findall(r'<mode>(.+?)</mode>', datum)
            tmEf = re.findall(r'<tmEf>(.+?)</tmEf>', datum)
            wf   = re.findall(r'<wf>(.+?)</wf>', datum)
            tmn  = re.findall(r'<tmn>(.+?)</tmn>', datum)
            tmx  = re.findall(r'<tmx>(.+?)</tmx>', datum)
            reli = re.findall(r'<reliability>(.+?)</reliability>', datum)
            #print(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reli[0])

            row = '{}, {}, {}, {}, {}, {}, {}, {}'.format(prov[0], city[0], mode[0], tmEf[0], wf[0], tmn[0], tmx[0], reli[0])
            # print(row)

            items = re.findall(r'<mode>(.+?)</mode>.+<tmEf>(.+?)</tmEf>.+<wf>(.+?)</wf>', datum, re.DOTALL)
            #print(items[0])

            t = items[0]
            print(t[0], t[1], t[2])

# findData()


def findLoc():
    for loc in locations:
        items = re.findall(r'<mode>(.+?)</mode>.+?<tmEf>(.+?)</tmEf>.+?<wf>(.+?)</wf>', loc, re.DOTALL)
        # print(items)
        # print(len(items))

        #for item in items:
        #    print(item)

        for mode, tmEf, wf in items:
            print(mode, tmEf, wf)

findLoc()
# 정부사이트
#   data.go.kr
#   data.seoul.go.kr
#   data.gg.go.kr
#   ...
# 포털사이트가 개발자센터
# SNS 개발자센터
# ...

# 네이버뉴스
# https://developers.naver.com 로그인

# 네이버 입장에서는 뉴스 데이터를 제3자에게 공개 : 위험
# 로그인해서 신청
# 애플리케이션 등록
#   애플리케이션 이름 : 마음대로
#   사용API : 검색
#   비로그인... : WEB설정 -> 웹사이트 주소 아무거나 하나
#   ClientID : Jxg2IcNrXA_1Bg2yfRiK
#   ClientSecret : TuOhPcVrRM

# Documents - 서비스API - 검색

from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from ljw.StringCleaner import StringCleaner

# request parameter
#   클라이언트가 서버에게 전달해주는 정보
# request header
#   클라이언트가 서버에게 전달해주는 정보
#   내부적으로 전달

# 인터넷 주소체계
# 프로토콜://서버주소[:포트번호]/폴더/.../파일?param변수명=param값&param변수명=param값&...

# 인터넷 주소에는 한글x
#   ㅋ -> %2D(URL인코딩)

q = quote("산불") # ㅋ -> %3D

# req header
h = {"X-Naver-Client-Id":"Jxg2IcNrXA_1Bg2yfRiK",
     "X-Naver-Client-Secret":"TuOhPcVrRM"} # {이름:값, 이름:값, ...}

hc = HTTPSConnection("openapi.naver.com") # 주소:포트
hc.request("GET", "/v1/search/news.xml?query=" + q,
           headers = h) # /폴더/파일?변수명=값
resBody = hc.getresponse().read()
hc.close()
# print(resBody.decode())

for i in fromstring(resBody).iter("item"):
    print(StringCleaner.clean(i.find("title").text) +
          " - " +
          StringCleaner.clean(i.find("description").text))

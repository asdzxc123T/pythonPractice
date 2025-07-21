# 기상청 웹사이트에 요청
# HTML/CSS/JavaScript
#   웹사이트
#   데이터를 사람들 보기 좋게 + 쓰기 좋게 보여주려고 - v
#   데이터를 AI훈련할 때 쓰게 주려고? - x
#   -> 파싱 힘듦
# XML/JSON
#   데이터 표현용
#   -> 파싱 편함

# parsing
# 받아온 데이터를 가공해서, 필요한 부분만 추출

# A가 B에게 데이터를 주는 상황
#   맑음2050북 형태로 주면
#   B 입장에서 작업을 어떻게...
#   맑음,20,50,북 형태로 주면
#   B가 작업하기 편함
# => A랑 B 사이에 뭔가 약속된 형식이 있어야
# => 국제표준
#       XML or JSON
#############################
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500
hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")
res = hc.getresponse()
resBody = res.read()
hc.close()
#############################
# XML(eXtended Markup Language)
#   데이터를 HTML 모양으로 표현해놓은
#   DOM(Document Object Model) 객체
#       <tagName attribute="value" attribute="value" ...> : startTag
#       text : text
#       </tagName> : endTag
weatherData = fromstring(resBody) # 시작
weathers = weatherData.iter("data") # <data>들
for w in weathers:
    print(w.find("hour").text) # <hour>
    print(w.find("temp").text) # <temp>
    print(w.find("wfKor").text) # <wfKor>
    print("-----")

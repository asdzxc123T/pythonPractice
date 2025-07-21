from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500
hc = HTTPSConnection("www.kma.go.kr")
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500")
res = hc.getresponse()
resBody = res.read()
hc.close()
####################################
# 오늘것만, kmaWeather.csv에
f = open("C:/ljw/kmaWeather.csv", "a", encoding="utf-8")
weatherData = fromstring(resBody) 
weathers = weatherData.iter("data") 
for w in weathers:
    if w.find("day").text == "1":
        break
    f.write("%s,%s,%s\n" % (w.find("hour").text, w.find("temp").text, w.find("wfKor").text))
f.close()
# 매일 아침마다 실행
# -> .bat 만들어서 바탕화면에 놓고 클릭해서 실행
# -> 윈도우 스케쥴러
# -> Linux 서버에 올려서 + 리눅스 스케쥴러
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

# 서울시 실시간 미세먼지데이터를 저장하는
# seoulDust.csv
# 2025,03,26,17,도심권,중구,70,17,보통
from datetime import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# 1) HTTP 통신 여부 확인
# 2) 파싱
# 3) 파일에 
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
hc.close()

now = datetime.today()
now = datetime.strftime(now, "%Y,%m,%d,%H")
f = open("C:/ljw/seoulDust.csv", "a", encoding="utf-8")
for w in fromstring(resBody).iter("row"):
    if w.find("IDEX_NM").text != None:
        date = w.find("MSRDT").text
        f.write(date[:4] + "," + date[4:6] + "," + date[6:8] + "," + date[8:10] +
                "," + w.find("MSRRGN_NM").text +
                "," + w.find("MSRSTE_NM").text +
                "," + w.find("PM10").text +
                "," + w.find("PM25").text +
                "," + w.find("IDEX_NM").text + "\n"
        )
f.close()
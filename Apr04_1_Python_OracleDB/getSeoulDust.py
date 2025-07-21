# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/

# 서울시 실시간 미세먼지데이터를 저장하는
# seoulDust.csv
# 2025,03,26,17,도심권,중구,70,17,보통
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring
from oracledb import connect

# 1) HTTP 통신 여부 확인
# 2) 파싱
# 3) 파일에 
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
hc.request("GET", "/575a4655496b636839386f58586542/xml/RealtimeCityAir/1/25/")
resBody = hc.getresponse().read()
hc.close()

con = connect("ljw100/91270290@195.168.9.68:1521/xe")

for w in fromstring(resBody).iter("row"):
    if w.find("IDEX_NM").text != None:
        # date = w.find("MSRDT").text
        sql = "insert into seoul_dust values (sysdate, "
        sql += "'%s', '%s', %s, %s, '%s')" % (w.find("MSRRGN_NM").text,
                                              w.find("MSRSTE_NM").text,
                                              w.find("PM10").text,
                                              w.find("PM25").text,
                                              w.find("IDEX_NM").text)
        cur = con.cursor()
        cur.execute(sql)
        cur.close()
con.commit()
con.close()
# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/548/20151101/

# 2015/01/01 ~ 2024/12/31 전체 지하철 운행정보 subway.csv로

# 1) HTTP 통신 테스트
# 2) 파싱
# 3) csv에 쓸 형태로 정리
#   2015,01,01,1호선,서울역,45000,30000
# 4) csv에 쓰기
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# key = "575a4655496b636839386f58586542"
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
f = open("C:/ljw/subway_ans.csv", "w", encoding="utf-8")
for yy in range(2015, 2025):
    for mm in range(1, 13):
        for dd in range(1, 32):
            when = "%d%02d%02d" % (yy, mm, dd)
            
            hc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/620/" + when)
            resBody = hc.getresponse().read()

            stations = fromstring(resBody).iter("row")
            for i in fromstring(resBody).iter("row"):
                f.write("%s,%s,%s,%s,%s,%s,%s\n" % (when[:4], when[4:6], when[6:8],
                                                    i.find("SBWY_ROUT_LN_NM").text,
                                                    i.find("SBWY_STNS_NM").text,
                                                    i.find("GTON_TNOPE").text,
                                                    i.find("GTOFF_TNOPE").text))
            print(when)
    
f.close()
hc.close()
# 2015 ~ 2024 버스 운행 정보
# csv로 저장
# 2015,01,01,100번(하계동~용산구청),명륜3가.성대입구,108,171

# 노선별 평균이용객수

# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/1/5/20151101/
from http.client import HTTPConnection
from json import loads

# key = "575a4655496b636839386f58586542"
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
f = open("C:/ljw/bus.csv", "a", encoding="utf-8")
for yy in range(2018, 2019):
    for mm in range(1, 13):
        for dd in range(1, 32):
            when = "%d%02d%02d" % (yy, mm, dd)
            start = 1
            end = 1000
            while True:
                url = "/575a4655496b636839386f58586542/json/CardBusStatisticsServiceNew/" + str(start) + "/" + str(end) + "/" + when
                hc.request("GET", url)
                resBody = hc.getresponse().read()
                result = loads(resBody)
                if "CardBusStatisticsServiceNew" in result:
                    for i in result["CardBusStatisticsServiceNew"]["row"]:
                        f.write("%s,%s,%s,%s,%s,%d,%d\n" % (when[:4], when[4:6], when[6:8],
                                                            i["RTE_NM"].replace(",", "."),
                                                            i["SBWY_STNS_NM"].replace(",", "."),
                                                            int(i["GTON_TNOPE"]),
                                                            int(i["GTOFF_TNOPE"])))
                else:
                    break
                start += 1000
                end += 1000
            print(when)
    
f.close()
hc.close()
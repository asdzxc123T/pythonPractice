# http://openapi.seoul.go.kr:8088/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/548/20151101/
import datetime
from http.client import HTTPConnection
from xml.etree.ElementTree import fromstring

# key = "575a4655496b636839386f58586542"
hc = HTTPConnection("openapi.seoul.go.kr", 8088)
date = datetime.datetime(2015,1,1)
f = open("C:/ljw/subway.csv", "w", encoding="utf-8")
while not date == datetime.datetime(2025,1,1):
    t = datetime.datetime.strftime(date, "%Y%m%d")
    print(t)
    hc.request("GET", "/575a4655496b636839386f58586542/xml/CardSubwayStatsNew/1/1000/" + t)
    resBody = hc.getresponse().read()

    for i in fromstring(resBody).iter("row"):
        f.write("%s,%s,%s,%s,%s,%s,%s\n" % (t[:4], t[4:6], t[6:8],
                                            i.find("SBWY_ROUT_LN_NM").text,
                                            i.find("SBWY_STNS_NM").text,
                                            i.find("GTON_TNOPE").text,
                                            i.find("GTOFF_TNOPE").text))
    date = date + datetime.timedelta(days=1)
f.close()
hc.close()
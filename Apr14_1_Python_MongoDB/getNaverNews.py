from http.client import HTTPSConnection
from urllib.parse import quote
from xml.etree.ElementTree import fromstring
from pymongo import MongoClient

def clean(txt):
    txt = txt.replace("&lt;b&gt;","")
    txt = txt.replace("&lt;/b&gt;","")
    txt = txt.replace("<b>","")
    txt = txt.replace("</b>","")
    txt = txt.replace("&apos;","")
    txt = txt.replace("&amp;","")
    txt = txt.replace("&quot;","")
    return txt

q = quote("취업")

h = {"X-Naver-Client-Id":"Jxg2IcNrXA_1Bg2yfRiK",
     "X-Naver-Client-Secret":"TuOhPcVrRM"}

hc = HTTPSConnection("openapi.naver.com")
hc.request("GET", "/v1/search/news.xml?query=" + q, headers = h)
resBody = hc.getresponse().read()
hc.close()
# print(resBody.decode())

con = MongoClient("195.168.9.68")
db = con.ljw
for i in fromstring(resBody).iter("item"):
    newsTitle = clean(i.find("title").text)
    newsDesc = clean(i.find("description").text)
    result = db.naver_news.insert_one({"title" : newsTitle, "desc" : newsDesc})
    if result.acknowledged:
        print(newsTitle + " - " + newsDesc)

con.close()
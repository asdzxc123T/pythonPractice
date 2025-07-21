from pymongo import MongoClient


con = MongoClient("195.168.9.68")
db = con.ljw

n_news = db.naver_news.find()

f = open("C:/ljw/naver_news.txt", "w", encoding="utf-8")
for n in n_news:
    f.write("%s\t%s\n" % (n["n_title"], n["n_desc"]))
f.close()
con.close()
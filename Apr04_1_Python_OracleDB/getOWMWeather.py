# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

from http.client import HTTPSConnection
from json import loads
from oracledb import connect

hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?lat=37.4939904&lon=126.7231945&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = hc.getresponse().read()
hc.close()
############################
weather = loads(resBody) # JSON -> Python 컬렉션
# 날씨
print(weather["weather"][0]["description"])
# 기온
print(weather["main"]["temp"])
# 습도
print(weather["main"]["humidity"])

con = connect("ljw100/91270290@195.168.9.68:1521/xe")
sql = "insert into weather values (sysdate, "
sql += "'%s', %s, %s, %s)" % (weather["weather"][0]["description"], 
                              weather["main"]["temp"],
                              weather["main"]["feels_like"],
                              weather["main"]["humidity"])
cur = con.cursor()
cur.execute(sql)

cur.close()
con.commit()
con.close()
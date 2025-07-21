# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

from http.client import HTTPSConnection
from json import loads

hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?lat=37.4939904&lon=126.7231945&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
resBody = hc.getresponse().read()
hc.close()
############################
weather = loads(resBody) # JSON -> Python 컬렉션
print(weather)
# 날씨
print(weather["weather"][0]["description"])
# 기온
print(weather["main"]["temp"])
# 습도
print(weather["main"]["humidity"])

# 오리지널 : AJAX
# Asynchronous Javascript And XML
# Javascript에서 쓰려고 만들어진 게 XML
# XML : 데이터를 HTML모양으로 표현
# JS에서 쓸건데 굳이 HTML 모양?
#   JS에서 쓸거면 JS모양으로 하는 게 편하겠지
# JSON(JavaScript Object Notation)
#   XML 후속
#   JS배열 : [1, 4, 34, 45] : Python list
#   JS객체 :
#       class 만들고...
#       {멤버변수명:값, 멤버변수명:값} : Python dict

#   모든 면에서 XML보다 상위호환
#       -> 현시점 데이터 표현은 JSON이 주력
#   근데 가독성은 XML이 더 나아서
#       -> XML은 각종 설정파일에 쓰임

# Python에서 XML

# https://www.google.co.kr/maps/place/%EB%B6%80%ED%8F%89%EB%AC%B8%ED%99%94%EC%9D%98%EA%B1%B0%EB%A6%AC/data=!4m6!3m5!1s0x357b7ddac1ccf1bf:0x542e956b2ac2c967!8m2!3d37.4939904!4d126.7231945!16s%2Fg%2F11j6hj8l0b?hl=ko&entry=ttu&g_ep=EgoyMDI1MDMyNS4wIKXMDSoASAFQAw%3D%3D
# !3d37.4939904!4d126.7231945!
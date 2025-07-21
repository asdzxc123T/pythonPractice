# dev.kakao.com
# 로그인
# 내 애플리케이션 - 애플리케이션 추가하기
#   아이콘 넘기고
#   앱 이름 알아서
#   회사명, 카테고리 알아서
#   -> 앱 키 -> REST API 키
#       e0bd46d9aea988808701f213a835bd46

#   문서 - 로컬 - REST API
#   키워드로 장소 검색하기

# https://dapi.kakao.com/v2/local/search/keyword.${FORMAT}
# FORMAT은 (xml, json)
# 솔데스크 좌표 : !3d37.5693582!4d126.9858652
from http.client import HTTPSConnection
from json import loads
from urllib.parse import quote

q = quote(input("뭐 : "))
y = 37.5693582
x = 126.9858652
url = "/v2/local/search/keyword.json?y=" + str(y) + "&x=" + str(x) + "&radius=500&query=" + q
hc = HTTPSConnection("dapi.kakao.com")
hc.request("GET", url,
           headers={"Authorization": "KakaoAK e0bd46d9aea988808701f213a835bd46"})
resBody = hc.getresponse().read()
hc.close()
result = loads(resBody)
# print(resBody.decode())
# print("-----")
# print(result)
for i in result["documents"]:
    print("상호명 : " + i["place_name"])
    print("주소 : " + i["address_name"])
    print("거리 : " + i["distance"] + "m")
    print("연락처 : " + i["phone"])
    print("-----")
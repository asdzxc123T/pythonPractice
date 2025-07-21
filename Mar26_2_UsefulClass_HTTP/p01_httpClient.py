# 컴퓨터 통신
#   Socket 통신(실시간) : 카톡(내 의지와 상관없이, 상대방이 보내면 옴)
#       Socket 서버 : Node.js 웹소켓서버에 특화
#       Socket 클라이언트 : JavaScript/React
#   HTTP 통신(실시간x) : 인터넷(내가 요청하면 거기에 대한 응답이 옴)
#       HTTP 서버 : Flask/Node.js
#           웹페이지 누군가가 요청하면 응답해주자
#           갖고 있는 데이터를 누군가가 요청하면 응답해주자
#           AI가 예측해낸 결과를 누군가가 요청하면 응답해주자
#       HTTP 클라이언트 : 
#           웹데이터 가져와서 AI 훈련용 데이터로 쟁여놓자(Python)
#           AI의 결과 웹페이지에 띄우자(JavaScript/React)

# server : 서비스를 제공하는 컴퓨터
# client : 서비스를 이용하는 컴퓨터

# 컴퓨터통신                vs      전화
#   protocol(통신방식)              전화, 영상통화, 카톡영상통화, ...
#   IP주소(142.250.71.228)          전화번호
#   Domain Name(www.google.com)     폰에 번호를 저장, 검색해서 찾기
#                                   => 글자로 저장 -> 의미가 생김
#   port(1~ 65536 서비스 구분)       ???        

# HTTP 통신(http or https(기본))
#   protocol : https
#   IP주소?
#   도메인네임 : www.weather.go.kr
#   포트 :
#       http : 80이 기본
#       https : 443이 기본 -> 안 써져 있으면 443
#   w/index.do
#       w : 폴더명
#       index.do : 파일명
# https://www.weather.go.kr/w/index.do

# Python에는 HTTP 통신 방식이 다양

from http.client import HTTPConnection, HTTPSConnection


# HTTPConnection
hc = HTTPSConnection("www.weather.go.kr") # 폴더/파일 전까지
# HTTP통신에서 요청 - GET 방식(기본)
#                  - HOST 방식(보안성 높일 때)
#               요청방식, 주소 남은부분 다
hc.request("GET", "/w/index.do")

res = hc.getresponse() # 응답
print(res)
resBody = res.read() # 응답내용
# print(resBody)
print(resBody.decode())

hc.close() # 세션(서버-클라이언트의 연결) 유지시간이 지나면 자동으로 끊기기는 함
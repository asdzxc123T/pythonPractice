# Python은 다 객체(다른 언어에서 말하는 기본형은 없음)
a = "aaaaa"
print(a)
print(type(a)) # class 확인, 자료형은 object
print(id(a)) # 객체 있는 heap 영역 주소값

# 문자열 그대로 나오게 할 때
b = """bbbbb
bbbbbb
   bbbb    bbb  b"""
print(b)

# 주석
"""
str 만들고 -> 메모리는 먹음
변수에 저장만 안 한 거 -> 주석이 아님
"""

class Dog:
    """
    클래스 매뉴얼
    """
    def bark(self):
        """
        bark에 대한 매뉴얼
        """
        print("멍")

# help(Dog) # 매뉴얼 보기
# help(print)
# Python 컨셉상
#   hybrid OOL : 메소드 형태가 아닌 것도
#   대체할 수 있으면 삭제 : 친절도가 떨어지는
# help(str)

c = "그니까 이제 알아서 해봐요"

# c가 그니까로 시작하는지
print(c.startswith("그니까"))

# c에서 이제 -> 다음부터
print(c.replace("이제", "다음부터"))

# c에 까가 몇번째에 있나
# print(c.index("까"))
print(c.find("까"))

# c에서 3번째 글자
print(c[2]) # 메소드 형태가 아닌...

# c에 해봐요가 있나
print(c.find("해봐요") != -1) # find로 대체 가능, contains가 따로 없음

# c 글자수
print(len(c))

# 글자 붙인다고 + 할 때마다 
# 기존 str 객체 GC 먹여 날리고 새로 만드는
# -> 메모리를 들쑤시는
# -> + 자제하는 게 좋은데, 여기는 Python
d = "저기"
print(d, id(d))
d += "뒤에다가"
print(d, id(d))
d += "이렇게에에에"
print(d, id(d))

# 데이터라고 받아오면 str 한 덩어리
e = "홍길동,김길동,이길동"
e2 = e.split(",") # , 기준으로 뜯어서 list로 반환 -> 정형데이터
print(e2)

f = "              zzz          "
print(f.strip()) # 쓸데없는 띄어쓰기 삭제
g = "~~~~~gggg~~~~"
print(g.strip("~")) # 쓸데없는 그거 삭제

# 정형데이터 : OracleDB
# 비정형데이터 : MongoDB
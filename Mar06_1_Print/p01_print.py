# ctrl + / : 주석 넣기
# ctrl + f5 : 실행
# alt + shift + f : 소스정렬
# alt + 화살표 위/아래 (vscode 전용 단축키) : 드래그된 소스 내용 이동
# alt + shift + 화살표 위/아래 : 줄 복사
# ctrl + shift + k : 줄 삭제
# ctrl + spaceBar : 자동완성

# -*- coding:utf-8 -*-
# 해당 소스가 utf-8로 인코딩되었다고 표시

# Java
# System.out.println("ㅋ"); = print("ㅋ")
# System.out.print("ㅋ"); = print("ㅋ", end="")
# System.out.printf("ㅋ");
# printf는 따로 없고 그냥 써먹으면 ex) %d

# 콘솔창에 출력 : 중간중간 테스트용
print("ㅋ")  # 출력하고 나서 줄 바뀜
print(
    "ㅎ", end=""
)  # 출력하고 나서 줄 안 바꾸기, end=을 통해서 따로 선언하지 않으면 개행문자가 자동
print("ㅇ")

# 인코딩 : 데이터 -> 전기신호
# 인코딩 방식 : 굉장히 다양(전세계적 utf-8 주력)
#   ㅋ  -A-> 10101 -A-> ㅋ
#       -B-> 01011 -C-> 뷁
#       -C-> 00001

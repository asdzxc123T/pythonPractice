# 자료형은 Python이 알아서 -> 잘 몰라도 된다
# 뭔가 입력하겠는데, 글자? 숫자?
# Python 입장에서는 str로 받아야 글자든 숫자든 다 소화 가능
# => 어디서 데이터를 받아오면 다 str
menu = input("메뉴명\t: ")
price = input("가격\t: ")
print("----------------------")
print(menu, type(menu)) # str
print(price, type(price), id(price)) # str
# type casting(형변환) => 자료형을 자신이 원하는 걸로 바꿔서
#   자료형(값)
#   => 사실은 객체 생성
price = int(price) 
print(price, type(price), id(price)) # int
print("%d원짜리 %s 먹자" % (price, menu))

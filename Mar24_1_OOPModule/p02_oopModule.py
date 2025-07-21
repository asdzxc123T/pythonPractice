# 1)
# # import 패키지명.모듈명
# import animal.pet
# # 패키지명.모듈명.클래스명(...)
# d = animal.pet.Dog("만득이")
# d.printInfo()

# 2)
# # import 패키지명.모듈명 as 별칭
# import animal.pet as ap
# # 별칭.클래스명(...)
# d = ap.Dog("만득이")
# d.printInfo()

# 3)
# # from 패키지명.모듈명 import 가져올거
# from animal.pet import Dog
# # 클래스명(...)
# d = Dog("만득이")
# d.printInfo()

# Windows에 PYTHONPATH를 설정하면 프로젝트도 인식
# 1) 직접 구축한 Linux에서 실행(on-premise)
# 2) 임대한 Linux에서 실행(Azure cloud)
from animal.pet import Dog

class Dog:
    pass

# import해온 class, 여기 있는 class 이름 중복되면?
# A에서 받아온 class, B에서 받아온 class 이름 중복되면?
# => 패키지명/모듈명이 아예 생략되는 3번으로는 해결 불가
# => 1, 2도 필요함
d = Dog("만득이")
d.printInfo()
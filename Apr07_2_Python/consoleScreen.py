from company.company import Company
from snack.snack import Snack

# V
#   front-end 개발자 : react(Python 말고)
#   디자이너 : 프로그래밍 언어 무관
class ConsoleScreen:
    def printCompanies(companies):
        print("-----")
        for c in companies:
            print("회사명 : %s" % c.name)
            print("주소 : %s" % c.addr)
            print("사장 : %s" % c.ceo)
            print("직원 수 : %d명" % c.emp)
            print("-----")
        print("-----")
    
    def printResult(result):
        print(result)
        print("-----")

    def printSnacks(snacks):
        print("-----")
        for s in snacks:
            print("과자 이름 : %s" % s.name)
            print("유통기한: %s" % s.exp)
            print("가격 : %d원" % s.price)
            print("용량 : %d원" % s.weight)
            print("회사명 : %s" % s.c_name)
            print("-----")
        print("-----")
    
    def printSnacksAndCompanies(snacks):
        print("-----")
        for s in snacks:
            print("과자 이름 : %s" % s.name)
            print("유통기한: %s" % s.exp)
            print("가격 : %d원" % s.price)
            print("용량 : %d원" % s.weight)
            print("회사명 : %s" % s.c_name)
            print("\t주소 : %s" % s.c_addr)
            print("\t사장 : %s" % s.c_ceo)
            print("\t직원 수 : %d명" % s.c_emp)
            print("-----")
        print("-----")

    def showMainMenu():
        print("1) 회사등록")
        print("2) 과자등록")
        print("3) 회사 전체 조회")
        print("4) 과자 전체 조회")
        print("5) 회사 조회")
        print("6) 과자 조회")
        print("7) 회사 검색")
        print("8) 과자 검색")
        print("9) 과자(+ 회사 정보) 검색")
        print("10) 과자 정보 수정")
        print("11) 과자 삭제")
        print("...")
        print("0) 종료")
        print("-----")
        return input("뭐 : ")
    
    def showRegCompanyMenu():
        print("-----")
        name = input("회사명 : ")
        addr = input("주소 : ")
        ceo = input("사장 : ")
        emp = input("직원수 : ")
        print("-----")
        return Company(name, addr, ceo, emp)
    
    def showRegSnackMenu():
        print("-----")
        name = input("과자 이름 : ")
        exp = input("유통기한 ('20250101'식으로 입력): ")
        price = input("가격 : ")
        weight = input("용량 : ")
        c_name = input("회사명 : ")
        print("-----")
        return Snack(name, exp, price, weight, c_name)
    
    def showSearchMenu():
        return input("검색어 : ")
    
    def showSelectDeleteMenu(snacks):
        for s in snacks:
            print("번호 : %s" % s.no)
            print("과자 이름 : %s" % s.name)
            print("유통기한: %s" % s.exp)
            print("가격 : %s원" % s.price)
            print("용량 : %s원" % s.weight)
            print("회사명 : %s" % s.c_name)
            print("-----")
        return input("삭제하고 싶은 과자의 번호 입력 : ")
    
    def showSelectPageMenu(pageCount):
        return input("페이지(1 ~ %d) : " % pageCount)
    
    def showSelectUpdateMenu(snacks):
        for s in snacks:
            print("번호 : %s" % s.no)
            print("과자 이름 : %s" % s.name)
            print("유통기한: %s" % s.exp)
            print("가격 : %s원" % s.price)
            print("용량 : %s원" % s.weight)
            print("회사명 : %s" % s.c_name)
            print("-----")
        return input("수정하고 싶은 과자의 번호 입력 : ")
    
    def getWhatToUpdate(s):
        print("1) 과자 이름 : %s" % s.name)
        print("2) 유통기한: %s" % s.exp)
        print("3) 가격 : %d원" % s.price)
        print("4) 용량 : %d원" % s.weight)
        print("5) 회사명 : %s" % s.c_name)
        print("-----")
        return input("바꿀 번호를 1 ~ 5 중 골라(0 입력 시 종료) : ")
    
    def getHowToUpdate(what):
        return input("어떻게?(유통기한은 20250101식으로 입력) : ")
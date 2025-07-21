from company.companyDAO import CompanyDAO
from snack.snackDAO import SnackDAO
from consoleScreen import ConsoleScreen

# DB 계정 1개를 여러명이 같이 쓰게 되는데
# 계정 하나를 동시에 쓸 수 있는 사람수는 제한되어 있음
# => 빨리 쓰고 빨리 치워야, 다른 사람이 그 계정을 쓸 수 있게 됨

# 1) 전체 과자 수 구하는 법 :
#       SELECT count(*) FROM apr07_snack 돌리면 나옴
#       Python - DB 서버 간의 통신을 해야
#       통신 횟수를 줄이면 좋은 거
#       -> 처음 한 번만 구해놓고 변동사항 생기면 수동 카운팅
# 2) 총 페이지 수 구하기
#       전체 과자 수 / 한 페이지 당 보여줄 과자 수 = 4.12312 올림
#       수동 카운팅 계산식이 복잡, DB 서버랑 무관
#       -> 조회 때마다
if __name__ == "__main__":
    sDAO = SnackDAO()
    cDAO = CompanyDAO()
    while True:
        menu = ConsoleScreen.showMainMenu()
        if menu == "1":
            company = ConsoleScreen.showRegCompanyMenu()
            ConsoleScreen.printResult(cDAO.reg(company))
        elif menu == "2":
            snack = ConsoleScreen.showRegSnackMenu()
            ConsoleScreen.printResult(sDAO.reg(snack))
        elif menu == "3":
            ConsoleScreen.printCompanies(cDAO.getAll())
        elif menu == "4":
            ConsoleScreen.printSnacks(sDAO.getAll())
        elif menu == "5":
            pageCount = cDAO.getPageCount("")
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            ConsoleScreen.printCompanies(cDAO.get(pageNo, ""))
        elif menu == "6":
            pageCount = sDAO.getPageCount("")
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            ConsoleScreen.printSnacks(sDAO.get(pageNo, ""))
        elif menu == "7":
            searchTerm = ConsoleScreen.showSearchMenu()
            pageCount = cDAO.getPageCount(searchTerm)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            ConsoleScreen.printCompanies(cDAO.get(pageNo, searchTerm))
        elif menu == "8":
            searchTerm = ConsoleScreen.showSearchMenu()
            pageCount = sDAO.getPageCount(searchTerm)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            ConsoleScreen.printSnacks(sDAO.get(pageNo, searchTerm))
        elif menu == "9":
            searchTerm = ConsoleScreen.showSearchMenu()
            pageCount = sDAO.getPageCount(searchTerm)
            if pageCount == 0:
                continue
            pageNo = ConsoleScreen.showSelectPageMenu(pageCount)
            snacks = sDAO.getWithCompany(pageNo, searchTerm)
            ConsoleScreen.printSnacksAndCompanies(snacks)
        elif menu == "10":
            searchTerm = ConsoleScreen.showSearchMenu()
            snacks = sDAO.getAllWithSearch(searchTerm)
            if len(snacks) == 0:
                continue
            ans = ConsoleScreen.showSelectUpdateMenu(snacks)
            while True:
                snack = sDAO.getCertainSnack(ans)
                what = ConsoleScreen.getWhatToUpdate(snack)
                if what == "0":
                    break
                how = ConsoleScreen.getHowToUpdate(what)
                sDAO.updateSnack(ans, what, how)
        elif menu == "11":
            searchTerm = ConsoleScreen.showSearchMenu()
            snacks = sDAO.getAllWithSearch(searchTerm)
            ans = ConsoleScreen.showSelectDeleteMenu(snacks)
            ConsoleScreen.printResult(sDAO.deleteSnack(ans))
        elif menu == "0":
            break
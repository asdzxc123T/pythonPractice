from math import ceil
from company.company import Company
from ljw.ljwDBManager import ljwDBManager

class CompanyDAO:
    def __init__(self):
        self.setAllCompanyCount()
        self.companyPerPage = 3

    def get(self, pageNo, searchTerm):
        companies = []
        pageNo = int(pageNo)
        start = (pageNo - 1) * self.companyPerPage + 1
        end = pageNo * self.companyPerPage
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select c_name, c_addr, c_ceo, c_emp "
            sql += "from ("
            sql += "    select rownum as rn, c_name, c_addr, c_ceo, c_emp "
            sql += "    from ("
            sql += "        select * "
            sql += "        from apr07_company "
            sql += "        where c_name like '%%%s%%' " % searchTerm
            sql += "        order by c_name"
            sql += "    )"
            sql += ") "
            sql += "where rn >= %d and rn <= %d" % (start, end)
            cur.execute(sql)
            for name, addr, ceo, emp in cur:
                c = Company(name, addr, ceo, emp)
                companies.append(c)
        except:
            companies = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return companies

    def getAll(self):
        companies = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from apr07_company order by c_name"
            cur.execute(sql)
            for name, addr, ceo, emp in cur:
                c = Company(name, addr, ceo, emp)
                companies.append(c)
        except:
            companies = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return companies
        
    def getPageCount(self, searchTxt):
        if searchTxt == "":
            companyCount = self.allCompanyCount
        else:
            companyCount = self.getSearchCompanyCount(searchTxt)
        return ceil(companyCount / self.companyPerPage)
    
    def getSearchCompanyCount(self, searchTerm):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select count(*) "
            sql += "from apr07_company "
            sql += "where c_name like '%%%s%%'" % searchTerm
            cur.execute(sql)
            for count in cur:
                return ceil(count[0] / self.companyPerPage)
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)

    def reg(self, company):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "insert into apr07_company "
            sql += "values('%s', '%s', '%s', %d)" % (company.name, company.addr, company.ceo, company.emp)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                return "등록 성공"
            else:
                return "등록 실패"
        except:
            return "등록 실패"
        finally:
            ljwDBManager.closeConCur(con, cur)
    
    def setAllCompanyCount(self):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select count(*) from apr07_company"
            cur.execute(sql)
            for count in cur:
                self.allCompanyCount = count[0]
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)
from datetime import datetime
from math import ceil
from snack.snack2 import Snack2
from snack.snack import Snack
from ljw.ljwDBManager import ljwDBManager

# 변수 만드는 이유 : 데이터 임시 저장
# 객체 만드는 이유 : 데이터를 실생활스럽게 저장
#   멤버변수가 없음 -> 저장할 게 없다
#   -> 객체 만들 필요가 없다
#   -> 객체를 안 만들고 쓸 수 있는 static 메소드 기반

class SnackDAO:
    def __init__(self):
        self.setAllSnackCount()
        self.snackPerPage = 3

    def deleteSnack(self, ans):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "delete from apr07_snack where s_no = %s" % ans
            cur.execute(sql)
            if cur.rowcount >= 1:
                con.commit()
                return "삭제 성공"
        except:
            return "삭제 실패"
        finally:
            ljwDBManager.closeConCur(con, cur)

    def get(self, pageNo, searchTerm):
        snacks = []
        pageNo = int(pageNo)
        start = (pageNo - 1) * self.snackPerPage + 1
        end = pageNo * self.snackPerPage
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select s_name, s_exp, s_price, s_weight, s_c_name "
            sql += "from ("
            sql += "    select rownum as rn, s_name, s_exp, s_price, s_weight, s_c_name "
            sql += "    from (select * "
            sql += "        from apr07_snack "
            sql += "        where s_name like '%%%s%%' " % searchTerm
            sql += "        order by s_name, s_price"
            sql += "    )"
            sql += ") "
            sql += "where rn >= %d and rn <= %d" % (start, end)
            cur.execute(sql)
            for name, exp, price, weight, c_name in cur:
                f_exp = datetime.strftime(exp, "%Y-%m-%d")
                s = Snack(name, f_exp, price, weight, c_name)
                snacks.append(s)
        except:
            snacks = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return snacks

    def getAll(self):
        snacks = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from apr07_snack order by s_name, s_price"
            cur.execute(sql)
            for no, name, exp, price, weight, c_name in cur:
                f_exp = datetime.strftime(exp, "%Y-%m-%d")
                s = Snack(name, f_exp, price, weight, c_name)
                snacks.append(s)
        except:
            snacks = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return snacks
        
    def getAllWithSearch(self, searchTerm):
        snacks = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from apr07_snack where s_name like '%%%s%%'" % searchTerm
            cur.execute(sql)
            for no, name, exp, price, weight, c_name in cur:
                f_exp = datetime.strftime(exp, "%Y-%m-%d")
                s = Snack2(no, name, f_exp, price, weight, c_name, 0, 0, 0)
                snacks.append(s)
        except:
            snacks = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return snacks
        
    def getCertainSnack(self, ans):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from apr07_snack where s_no = %d" % int(ans)
            cur.execute(sql)
            for no, name, exp, price, weight, c_name in cur:
                f_exp = datetime.strftime(exp, "%Y-%m-%d")
                return Snack2(no, name, f_exp, price, weight, c_name, 0, 0, 0)
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)
        
    def getPageCount(self, searchTxt):
        if searchTxt == "":
            snackCount = self.allSnackCount
        else:
            snackCount = self.getSearchSnackCount(searchTxt)
        return ceil(snackCount / self.snackPerPage)
    
    def getSearchSnackCount(self, searchTerm):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select count(*) from apr07_snack "
            sql += "where s_name like '%%%s%%'" % searchTerm
            cur.execute(sql)
            for count in cur:
                return ceil(count[0] / self.snackPerPage)
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)

    def getWithCompany(self, pageNo, searchTerm):
        snacks = []
        pageNo = int(pageNo)
        start = (pageNo - 1) * self.snackPerPage + 1
        end = pageNo * self.snackPerPage

        # join
        #   A 테이블 : 100개
        #   B 테이블 : 100개
        #   A, B join 시키면 10000개로 데이터를 폭증시켜서 RAM에 넣고...
        #   1) 과자만 가져오고, 회사는 Python으로 따로 가져와서
        #       과자가 3개라 치면
        #           조회 1      조회 3  -> 총 조회 횟수가 N + 1번이 됨
        #   2) A, B에 있는 거 다 가져와서 join시키지 말고
        #       필요한 것들만 가져와서 join

        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select s_name, s_exp, s_price, s_weight, s_c_name, c_addr, c_ceo, c_emp "
            sql += "from ("
            sql += "    select s_name, s_exp, s_price, s_weight, s_c_name "
            sql += "    from ("
            sql += "        select rownum as rn, s_name, s_exp, s_price, s_weight, s_c_name "
            sql += "        from ("
            sql += "            select * "
            sql += "            from apr07_snack "
            sql += "            where s_name like '%%%s%%' " % searchTerm
            sql += "            order by s_name, s_price"
            sql += "        ) "
            sql += "    ) "
            sql += "    where rn >= %d and rn <= %d" % (start, end)
            sql += "), ("
            sql += "    select * "
            sql += "    from apr07_company "
            sql += "    where c_name in ("
            sql += "        select s_c_name "
            sql += "        from ("
            sql += "            select rownum as rn, s_name, s_exp, s_price, s_weight, s_c_name "
            sql += "            from ("
            sql += "                select * "
            sql += "                from apr07_snack "
            sql += "                where s_name like '%%%s%%' " % searchTerm
            sql += "                order by s_name, s_price"
            sql += "            ) "
            sql += "        ) "
            sql += "        where rn >= %d and rn <= %d" % (start, end)
            sql += "    ) "
            sql += ") "
            sql += "where s_c_name = c_name"

            cur.execute(sql)
            for name, exp, price, weight, c_name, addr, ceo, emp in cur:
                f_exp = datetime.strftime(exp, "%Y-%m-%d")
                s = Snack2(0, name, f_exp, price, weight, c_name, addr, ceo, emp)
                snacks.append(s)
        except:
            snacks = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return snacks

    def reg(self, snack):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "insert into apr07_snack "
            sql += "values(apr07_snack_seq.nextval, '%s', to_date('%s', 'YYYYMMDD'), %d, %d, '%s')" % (snack.name, snack.exp, snack.price, snack.weight, snack.c_name)
            cur.execute(sql)
            if cur.rowcount == 1:
                con.commit()
                self.allSnackCount += 1
                return "등록 성공"
            else:
                return "등록 실패"
        except:
            return "등록 실패"
        finally:
            ljwDBManager.closeConCur(con, cur)
    
    def setAllSnackCount(self):
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select count(*) from apr07_snack"
            cur.execute(sql)
            for count in cur:
                self.allSnackCount = count[0]
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)

    def updateSnack(self, ans, what, how):
        e = [None, "s_name", "s_exp", "s_price", "s_weight", "s_c_name"]
        what = int(what)
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            if what == "2":
                how = "to_date('%s', 'YYYY-MM-DD')" % how
            elif what == "1" or what == "5":
                how = "'" + str(how) + "'"
            sql = "update apr07_snack set %s = %s where s_no = %s" % (e[what], how, ans)
            cur.execute(sql)
            if cur.rowcount >= 1:
                con.commit()
        except:
            pass
        finally:
            ljwDBManager.closeConCur(con, cur)
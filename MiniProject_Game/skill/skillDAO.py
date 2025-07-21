from skill.skill import Skill
from ljw.ljwDBManager import ljwDBManager


class SkillDAO:
    def getPlayerSkill(player):
        skills = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from gameSkill where s_no in ("
            sql += "    select r_s_no "
            sql += "    from rel_c_s "
            sql += "    where r_c_no = %d" % player.no
            sql += ")"
            cur.execute(sql)
            for no, name, type, costHP, costMP, mul, price in cur:
                s = Skill(no, name, type, costHP, costMP, mul, price)
                skills.append(s)
        except:
            skills = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return skills

    def getAllSkill():
        skills = []
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from gameSkill"
            cur.execute(sql)
            for no, name, type, costHP, costMP, mul, price in cur:
                s = Skill(no, name, type, costHP, costMP, mul, price)
                skills.append(s)
        except:
            skills = ["검색 실패"]
        finally:
            ljwDBManager.closeConCur(con, cur)
            return skills
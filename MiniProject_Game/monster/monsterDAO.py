from random import randint
from monster.monster import Monster
from ljw.ljwDBManager import ljwDBManager


class MonsterDAO:
    def getRandomMonster(floor):
        monsters = []
        if floor > 5:
            min = floor - 2
        else:
            min = 1
        try:
            con, cur = ljwDBManager.makeConCur("ljw100/91270290@195.168.9.124:1521/xe")
            sql = "select * from monster where m_floor >= %d and m_floor <= %d order by m_no" % (min, floor)
            cur.execute(sql)
            for no, name, type, hp, mp, baseAttack, baseDefense, reqDex, exp, gold, floor in cur:
                s = Monster(no, name, type, hp, mp, baseAttack, baseDefense, reqDex, exp, gold, floor)
                monsters.append(s)
            t = randint(0, len(monsters) - 1)
            return monsters[t]
        except:
            return "검색 실패"
        finally:
            ljwDBManager.closeConCur(con, cur)
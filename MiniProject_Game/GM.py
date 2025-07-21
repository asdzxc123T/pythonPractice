from random import randint


class GM:
    def playerBasicAttack(player, monster, equipWeapon):
        d = player.baseAttack + equipWeapon.phyDmg - monster.baseDefense
        if d <= 0:
            d = 1
        monster.currentHp -= d
        return d
    
    def playerSkillAttack(player, monster, equipWeapon, skill):
        if skill.type == 1:
            d = (player.baseAttack + equipWeapon.phyDmg) * skill.mul - monster.baseDefense
        else:
            d = (player.int + equipWeapon.magDmg) * skill.mul - monster.baseDefense
        if d <= 0:
            d = 1
        player.currentHp -= skill.costHP
        player.currentMp -= skill.costMP
        monster.currentHp -= d
        return d
    
    def ableToSkill(player, skill):
        return player.currentHp > skill.costHP and player.currentMp >= skill.costMP
    
    def resetHpMp(player):
        player.currentHp = player.hp
        player.currentMp = player.mp

    def playerAlive(player):
        return player.currentHp > 0
    
    def monsterAlive(monster):
        return monster.currentHp > 0
    
    def playerFaster(player, monster):
        return player.dex >= monster.reqDex
    
    def monsterAttack(monster, player, equipArmor):
        if monster.type == 1:
            d = monster.baseAttack - (player.baseDefense + equipArmor.phyDef)
        else:
            d = monster.baseAttack - (player.int + equipArmor.magDef)
        if d <= 0:
            d = 1
        player.currentHp -= d
        return d

    def randomItem(itemList):
        return itemList[randint(0, len(itemList))]
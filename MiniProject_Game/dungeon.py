from random import randint
from GM import GM
from armor.armorDAO import ArmorDAO
from weapon.weaponDAO import WeaponDAO
from gameCharacter.gcDAO import GCDAO
from monster.monsterDAO import MonsterDAO
from consoleScreen import ConsoleScreen
from GameOptions import reqExp

class Dungeon:
    def __init__(self):
        self.floor = 20
    
    def dungeon(self, player, equipWeapon, equipArmor, equipSkill):
        for floor in range (1, self.floor + 1):
            while True:
                decision = ConsoleScreen.showDungeonMenu(floor, self.floor, player)
                if decision == "1" or decision == "2":
                    break
            if decision == "1":
                encounter = randint(1, 10)
                if 1 <= encounter <= 8:
                    monster = MonsterDAO.getRandomMonster(floor)
                    if not self.fight(player, monster, equipWeapon, equipArmor, equipSkill):
                        GM.resetHpMp(player)
                        break
                    GCDAO.getGoldAndExp(player, monster)
                    ConsoleScreen.showGoldAndExp(monster)
                    if player.exp >= reqExp[player.lv] and player.lv != 10:
                        s, d, i = GCDAO.levelUp(player)
                        ConsoleScreen.showLevelUp(player, s, d, i)
                elif 9 <= encounter <= 10:
                    num = randint(1, 20)
                    if not self.event(player, equipWeapon, equipArmor, equipSkill, floor, num):
                        GM.resetHpMp(player)
                        break
            elif decision == "2":
                GM.resetHpMp(player)
                break

    def fight(self, player, monster, equipWeapon, equipArmor, equipSkill):
        ConsoleScreen.showEncounter(monster, 1)
        while GM.playerAlive(player) and GM.monsterAlive(monster):
            if GM.playerFaster(player, monster):
                if self.playerChoice(player, monster, equipWeapon, equipArmor, equipSkill):
                    self.monsterChoice(monster, player, equipArmor)
            else:
                if self.monsterChoice(monster, player, equipArmor):
                    self.playerChoice(player, monster, equipWeapon, equipArmor, equipSkill)
        if GM.playerAlive(player):
            return 1
        ConsoleScreen.showResult(GCDAO.loseGold(player))
        return 0
    
    def playerChoice(self, player, monster, equipWeapon, equipArmor, equipSkill):
        choice = ConsoleScreen.playerChoice(player, monster, equipWeapon, equipArmor)
        if choice == "1":
            d = GM.playerBasicAttack(player, monster, equipWeapon)
            ConsoleScreen.printDamage(player.name, monster.name, d)
        elif choice == "2":
            skill = ConsoleScreen.playerSkillChoice(equipSkill)
            if not GM.ableToSkill(player, skill):
                ConsoleScreen.printNotEnoughCost()
                return self.playerChoice(player, monster, equipWeapon, equipSkill)
            d = GM.playerSkillAttack(player, monster, equipWeapon, skill)
            ConsoleScreen.printDamage(player.name, monster.name, d)
        elif choice == "3":
            player.currentHp = 0
            return 0
        if monster.currentHp <= 0:
            return 0
        return 1
    
    def monsterChoice(self, monster, player, equipArmor):
        d = GM.monsterAttack(monster, player, equipArmor)
        ConsoleScreen.printDamage(monster.name, player.name, d)
        if player.currentHp <= 0:
            return 0
        return 1
    
    def event(self, player, equipWeapon, equipArmor, equipSkill, floor, num):
        if num == 1:
            weaponList = WeaponDAO.getAllWeapon()
            randomItem = GM.randomItem(weaponList)
            replaceItem = ConsoleScreen.foundWeapon(player, randomItem, equipWeapon)
            if replaceItem == "1":
                ConsoleScreen.showResult(GCDAO.updateCharacter(player, randomItem, 1))
                equipWeapon = WeaponDAO.getPlayerWeapon(player)
        elif num == 2:
            armorList = ArmorDAO.getAllArmor()
            randomItem = GM.randomItem(armorList)
            replaceItem = ConsoleScreen.foundArmor(player, randomItem, equipArmor)
            if replaceItem == "1":
                ConsoleScreen.showResult(GCDAO.updateCharacter(player, randomItem, 2))
                equipArmor = ArmorDAO.getPlayerArmor(player)
        else:
            monster = MonsterDAO.getRandomMonster(floor)
            helpThem = ConsoleScreen.foundSomeone(monster)
            if helpThem == "1":
                if not self.fight(player, monster, equipWeapon, equipArmor, equipSkill):
                    return 0
                g = GCDAO.getGift(player)
                ConsoleScreen.getGift(g)
        return 1
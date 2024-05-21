import lcg
import time

def atribut(monster,level):
    def upgrade(skill):
        skill_monster = int(monster[skill]) + ((int(monster[skill])*(level-1))//10)
        return skill_monster
    
    def_power_up = upgrade('def_power')
    if def_power_up > 50:
        def_power_up = 50

    return [upgrade('atk_power'),def_power_up,upgrade('hp')]

def level_hp(monster,level):
    def upgrade(skill):
        skill_monster = int(monster[skill]) + ((int(monster[skill])*(level-1))//10)
        return skill_monster
    
    return upgrade('hp')

def attack(monster_enemy,atk_power):
    time.sleep(0.001)
    damage_dealt = lcg.randint1(int(atk_power*(0.7)),int(atk_power*(1.3)))*(1-(monster_enemy[1]//100))
    monster_enemy[2] -= damage_dealt
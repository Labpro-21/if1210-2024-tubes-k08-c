import lcg

def atribut(monster,level):
    def upgrade(skill):
        skill_monster = int(monster[skill]) + ((int(monster[skill])*(level-1))//10)
        return skill_monster

    return [upgrade('atk_power'),upgrade('def_power'),upgrade('hp')]

def level_hp(monster,level):
    def upgrade(skill):
        skill_monster = int(monster[skill]) + ((int(monster[skill])*(level-1))//10)
        return skill_monster
    
    return upgrade('hp')

def attack(monster_enemy,atk_power):
    monster_enemy[2] -= lcg.randint1(int(atk_power*(0.7)),int(atk_power*(1.3)))*(1-(monster_enemy[1]//100))
    return monster_enemy[2]
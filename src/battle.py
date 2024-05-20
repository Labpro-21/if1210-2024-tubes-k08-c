import lcg
import monster
import potion
import time

# Parameter user untuk file user.csv
# Parameter monster_inventory untuk file monster_inventory.csv
# Parameter monster_dict untuk file monster.csv
# Parameter id merupakan id dari pemain

item_inventory = [{'user_id': '2', 'type': 'strength', 'quantity': '5'}, {'user_id': '2', 'type': 'resilience', 'quantity': '3'}, {'user_id': '3', 'type': 'resilience', 'quantity': '7'}, {'user_id': '4', 'type': 'healing', 'quantity': '3'}, {'user_id': '5', 'type': 'strength', 'quantity': '20'}]
monster_inventory = [{'user_id': '2', 'monster_id': '1', 'level': '1'}, {'user_id': '3', 'monster_id': '2', 'level': '2'}, {'user_id': '3', 'monster_id': '3', 'level': '1'}, {'user_id': '4', 'monster_id': '4', 'level': '1'}, {'user_id': '5', 'monster_id': '5', 'level': '5'}]
monster_dict = [{'id': '1', 'type': 'Pikachow', 'atk_power': '125', 'def_power': '10', 'hp': '600'}, {'id': '2', 'type': 'Bulbu', 'atk_power': '50', 'def_power': '50', 'hp': '1200'}, {'id': '3', 'type': 'Zeze', 'atk_power': '300', 'def_power': '10', 'hp': '100'}, {'id': '4', 'type': 'Zuko', 'atk_power': '100', 'def_power': '25', 'hp': '800'}, {'id': '5', 'type': 'Chacha', 'atk_power': '80', 'def_power': '30', 'hp': '7006'}]
user = [{'id': '1', 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin', 'oc': '0'}, {'id': '2', 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent', 'oc': '9999'}, {'id': '3', 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent', 'oc': '0'}, {'id': '4', 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent', 'oc': '1337'}, {'id': '5', 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent', 'oc': '6699'}]

def user_id_monster(monster_inventory : list[dict[int]], id: int) -> list[dict[int]]: # fungsi untuk mengambil monster bergantung pada user_id
    list_monster = []
    for i in monster_inventory:
        if i['user_id'] == id:
            list_monster.append(i)

    return list_monster

def name_user(id: int, user: list[dict[int]]) -> str: # fungsi untuk menentukan nama dari id yang diberikan
    for i in user:
        if i['id'] == id:
            return i['username']

def select_monster (id: int, user: list[dict],list_monster_user):
    def monster_n(n): # fungsi untuk listing monster sesuai dengan yang dimiliki player
        return monster_dict[int(list_monster_user[n]["monster_id"])-1]
    print("""============ MONSTER LIST ============""")
    for i in range(len(list_monster_user)):
        print(f"{i+1}. {monster_n(i)['type']}")

    while True:
        pilihan = int(input("\nPilih monster untuk bertarung: "))
        if pilihan > len(list_monster_user):
            print("Pilihan nomor tidak tersedia!")
        else:
            break

    list_player_monster = monster.atribut(monster_n(pilihan-1),int(list_monster_user[pilihan-1]['level']))
    max_hp_player = monster.level_hp(monster_n(pilihan-1),int(list_monster_user[pilihan-1]['level']))
    base_hp_player = monster.level_hp(monster_n(pilihan-1),1)

    print(f"""\n          /\\----/\\_   
         /         \\   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \\  |   |   |
         |  |   |   |
          \\._\\   \\._\\ 

RAWRRR, Agent {name_user(id,user)} mengeluarkan monster {monster_n(pilihan-1)['type']} !!!

Name : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}""")
    return pilihan,list_player_monster,max_hp_player,base_hp_player

def battle(id: int, user: list[dict], item_inventory: list[dict], monster_inventory: list[dict], monster_dict: list[int,str,int,int,int], level: int, pilihan: int,list_player_monster: list[int],max_hp_player: int,base_hp_player: int) -> None: # fungsi utama
    # untuk battel aja yg masukan level hinnga base_hp_player masukin aja 0
    random_num = lcg.randint1(0,len(monster_dict)-1)
    type_monster = monster_dict[random_num]
    if level ==0:
        level_monster = lcg.randint1(1,5)
    else:
        level_monster = level
    skill_monster_enemy = monster.atribut(type_monster,level_monster)
    list_monster_user = user_id_monster(monster_inventory,id)

    def monster_n(n): # fungsi untuk listing monster sesuai dengan yang dimiliki player
        return monster_dict[int(list_monster_user[n]["monster_id"])-1]
    
    print(f"""           
           _/\\----/\\   
          /         \\     /\\
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \\  |  |
        /   `^^^^^'    \\ |  |
      ./  /|            \\|  |_
     /   / |         |\\__     /
     \\  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
RAWRRR, Monster {type_monster['type']} has appeared !!!

Name      : {type_monster['type']}
ATK Power : {skill_monster_enemy[0]}
DEF Power : {skill_monster_enemy[1]}
HP        : {skill_monster_enemy[2]}
Level     : {level_monster}
""")
    if level == 0:
        pilihan,list_player_monster,max_hp_player,base_hp_player = select_monster(id,user,list_monster_user)

    hp_enemy = skill_monster_enemy[2]
    hp_user = list_player_monster[2]

    turn_num = 1
    num_potion = [0,0,0]
    while True:
        print(f"""
============ TURN {turn_num} {monster_n(pilihan-1)['type']} ============
              
1. Attack
2. Use Potion
3. Quit
""")
            
        pilihan_2 = int(input("Select a command: "))
        if pilihan_2 == 1:
            hp_before = skill_monster_enemy[2]
            monster.attack(skill_monster_enemy,int(list_player_monster[0]))
            hp_after = skill_monster_enemy[2]
            damage_dealt = hp_before - hp_after

            if skill_monster_enemy[2] <= 0:
                skill_monster_enemy[2] = 0
            
            print(f"""
SCHWINKKK, your {monster_n(pilihan-1)['type']} attacks {type_monster['type']} !!!
Enemy {type_monster['type']} takes {damage_dealt} damage""")
            time.sleep(2)
            print(f"""
Name      : {type_monster['type']}
ATK Power : {skill_monster_enemy[0]}
DEF Power : {skill_monster_enemy[1]}
HP        : {skill_monster_enemy[2]}
Level     : {level_monster}
""")
            
            if skill_monster_enemy[2] <= 0:
                print(f"Congratulations, you have successfully defeated {type_monster['type']} !!!")
                if level == 0:
                    add_oc_coin = lcg.randint1(5*level_monster,30*level_monster)
                    user[int(id)-1]["oc"] = str(int(user[int(id)-1]["oc"])+add_oc_coin)
                    print(f"Total OC earned: {add_oc_coin}")
                else:
                    result = "menang"
                    damage_dealt = hp_enemy
                    damage_received = hp_user - list_player_monster[2]
                    return(result,damage_dealt,damage_received)
                break
            else:
                hp_before_2 = list_player_monster[2]
                monster.attack(list_player_monster,skill_monster_enemy[0])
                hp_after_2 = list_player_monster[2]
                damage_dealt_2 = hp_before_2 - hp_after_2
                if list_player_monster[2] <= 0:
                    list_player_monster[2] = 0
                print(f"""
============ TURN {turn_num} {type_monster['type']} ============
SCHWINKKK, enemy {type_monster['type']} attacks your {monster_n(pilihan-1)['type']} !!!
Your {monster_n(pilihan-1)['type']} takes {damage_dealt_2} damage""")
                time.sleep(2)
                print(f"""
Name      : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}
""")
                if list_player_monster[2] <= 0:
                    print(f"Nooo, You are defeated by the monster {type_monster['type']}. Don't give up, try again!!!")
                    if level != 0:
                        result = "kalah"
                        damage_dealt = hp_enemy - skill_monster_enemy[2]
                        damage_received = hp_user
                        return(result,damage_dealt,damage_received)
                    break
                else:
                    turn_num += 1

        elif pilihan_2 == 2:
            hp_before_potion = list_player_monster[2]
            aktivate = potion.ui_potion(item_inventory,monster_n(pilihan-1)['type'],list_player_monster,base_hp_player,max_hp_player,id,num_potion)
            hp_after_potion = list_player_monster[2]
            if aktivate:
                hp_user += (hp_after_potion-hp_before_potion)
                hp_before_3 = list_player_monster[2]
                monster.attack(list_player_monster,skill_monster_enemy[0])
                hp_after_3 = list_player_monster[2]
                damage_dealt_3 = hp_before_3 - hp_after_3

                if list_player_monster[2] <= 0:
                    list_player_monster[2] = 0
                print(f"""
============ TURN {turn_num} {type_monster['type']} ============

SCHWINKKK, enemy {type_monster['type']} attacks your {monster_n(pilihan-1)['type']} !!!
Your {monster_n(pilihan-1)['type']} takes {damage_dealt_3} damage""")
                time.sleep(2)
                print(f"""
Name      : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}""")
                if list_player_monster[2] <= 0:
                    print(f"Yahhh, You are defeated by the monster {type_monster['type']}. Don't give up, try again!!!")
                    if level != 0:
                        result = "kalah"
                        damage_dealt = hp_enemy - skill_monster_enemy[2]
                        damage_received = hp_user
                        return(result,damage_dealt,damage_received)
                    break
                else:
                    turn_num += 1
        
        elif pilihan_2 == 3:
            print("You have successfully escaped the BATTLE!")
            if level != 0:
                result = "quit"
                damage_dealt = hp_enemy - skill_monster_enemy[2]
                damage_received = hp_user - list_player_monster[2]
                return(result,damage_dealt,damage_received)
            break
        else:
            print("""
Your input is invalid, please input again.""")

# print(load.csv_to_dict(os.path.join("data/","init/","user.csv")))
# battle('3',user,item_inventory,monster_inventory,monster_dict)
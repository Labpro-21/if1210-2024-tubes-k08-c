import lcg
import os
import monster
import tabel
import potion
import load

# Parameter user untuk file user.csv
# Parameter monster_inventory untuk file monster_inventory.csv
# Parameter monster_dict untuk file monster.csv
# Parameter id merupakan id dari pemain

item_inventory = [{'user_id': '2', 'type': 'strength', 'quantity': '5'}, {'user_id': '2', 'type': 'resilience', 'quantity': '3'}, {'user_id': '3', 'type': 'resilience', 'quantity': '7'}, {'user_id': '4', 'type': 'healing', 'quantity': '3'}, {'user_id': '5', 'type': 'strength', 'quantity': '20'}]
monster_inventory = [{'user_id': '2', 'monster_id': '1', 'level': '1'}, {'user_id': '3', 'monster_id': '2', 'level': '2'}, {'user_id': '3', 'monster_id': '3', 'level': '1'}, {'user_id': '4', 'monster_id': '4', 'level': '1'}, {'user_id': '5', 'monster_id': '5', 'level': '5'}]
monster_dict = [{'id': '1', 'type': 'Pikachow', 'atk_power': '125', 'def_power': '10', 'hp': '600'}, {'id': '2', 'type': 'Bulbu', 'atk_power': '50', 'def_power': '50', 'hp': '1200'}, {'id': '3', 'type': 'Zeze', 'atk_power': '300', 'def_power': '10', 'hp': '100'}, {'id': '4', 'type': 'Zuko', 'atk_power': '100', 'def_power': '25', 'hp': '800'}, {'id': '5', 'type': 'Chacha', 'atk_power': '80', 'def_power': '30', 'hp': '7006'}]
user = [{'id': '1', 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin', 'oc': '0'}, {'id': '2', 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent', 'oc': '9999'}, {'id': '3', 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent', 'oc': '0'}, {'id': '4', 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent', 'oc': '1337'}, {'id': '5', 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent', 'oc': '6699'}]

def user_id_monster(monster_inventory,id): # fungsi untuk mengambil monster bergantung pada user_id
    list_monster = []
    for i in monster_inventory:
        if i["user_id"] == str(id):
            list_monster.append(i)

    return list_monster

def name_user(id,user): # fungsi untuk menentukan nama dari id yang diberikan
    for i in user:
        if i['id'] == str(id):
            return i['username']

def battle(id,user,item_inventory,monster_inventory,monster_dict): # fungsi utama
    random_num = lcg.randint1(0,len(monster_dict)-1)
    type_monster = monster_dict[random_num]
    level_monster = lcg.randint1(1,5)
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
RAWRRR, Monster {type_monster['type']} telah muncul !!!

Name      : {type_monster['type']}
ATK Power : {skill_monster_enemy[0]}
DEF Power : {skill_monster_enemy[1]}
HP        : {skill_monster_enemy[2]}
Level     : {level_monster}

============ MONSTER LIST ============""")
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

    turn_num = 1
    num_potion = [0,0,0]
    while True:
        print(f"""
============ TURN {turn_num} {monster_n(pilihan-1)['type']} ============
              
1. Attack
2. Use Potion
3. Quit
""")
            
        pilihan_2 = int(input("Pilih perintah: "))
        if pilihan_2 == 1:
            monster.attack(skill_monster_enemy,int(list_player_monster[0]))

            if skill_monster_enemy[2] <= 0:
                skill_monster_enemy[2] = 0
            
            print(f"""\n{monster_n(pilihan-1)['type']}, menyerang {type_monster['type']} !!!

Name      : {type_monster['type']}
ATK Power : {skill_monster_enemy[0]}
DEF Power : {skill_monster_enemy[1]}
HP        : {skill_monster_enemy[2]}
Level     : {level_monster}
""")
            
            if skill_monster_enemy[2] <= 0:
                print(f"Selamat, Anda berhasil mengalahkan monster {type_monster['type']} !!!")
                add_oc_coin = lcg.randint1(5*level_monster,30*level_monster)
                user[int(id)-1]["oc"] = str(int(user[int(id)-1]["oc"])+add_oc_coin)
                print(f"Total OC yang diperoleh: {add_oc_coin}")
                break
            else:
                monster.attack(list_player_monster,skill_monster_enemy[0])
                if list_player_monster[2] <= 0:
                    list_player_monster[2] = 0
                print(f"""
============ TURN {turn_num} {type_monster['type']} ============
SCHWINKKK, {type_monster['type']} menyerang {monster_n(pilihan-1)['type']} !!!

Name      : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}
""")
                if list_player_monster[2] <= 0:
                    print("Yahhh, Anda dikalahkan monster Zuko. Jangan menyerah, coba lagi !!!")
                    break
                else:
                    turn_num += 1

        elif pilihan_2 == 2:
            aktivate = potion.ui_potion(item_inventory,monster_n(pilihan-1)['type'],list_player_monster,base_hp_player,max_hp_player,id,num_potion)
            if aktivate:
                monster.attack(list_player_monster,skill_monster_enemy[0])
                if list_player_monster[2] <= 0:
                    list_player_monster[2] = 0
                print(f"""
============ TURN {turn_num} {type_monster['type']} ============

SCHWINKKK, {type_monster['type']} menyerang {monster_n(pilihan-1)['type']} !!!

Name      : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}""")
                if list_player_monster[2] <= 0:
                    print("Yahhh, Anda dikalahkan monster Zuko. Jangan menyerah, coba lagi !!!")
                    break
                else:
                    turn_num += 1
        
        elif pilihan_2 == 3:
            print("Anda berhasil kabur dari BATTLE!")
            break

# print(load.csv_to_dict(os.path.join("data/","init/","user.csv")))
# battle('3',user,item_inventory,monster_inventory,monster_dict)
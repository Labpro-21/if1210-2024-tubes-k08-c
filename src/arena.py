import battle
import monster
import potion
import lcg
item_inventory = [{'user_id': '2', 'type': 'strength', 'quantity': '5'}, {'user_id': '2', 'type': 'resilience', 'quantity': '3'}, {'user_id': '3', 'type': 'resilience', 'quantity': '7'}, {'user_id': '4', 'type': 'healing', 'quantity': '3'}, {'user_id': '5', 'type': 'strength', 'quantity': '20'}]
monster_inventory = [{'user_id': '2', 'monster_id': '1', 'level': '1'}, {'user_id': '3', 'monster_id': '2', 'level': '2'}, {'user_id': '3', 'monster_id': '3', 'level': '1'}, {'user_id': '4', 'monster_id': '4', 'level': '1'}, {'user_id': '5', 'monster_id': '5', 'level': '5'}]
monster_dict = [{'id': '1', 'type': 'Pikachow', 'atk_power': '125', 'def_power': '10', 'hp': '600'}, {'id': '2', 'type': 'Bulbu', 'atk_power': '50', 'def_power': '50', 'hp': '1200'}, {'id': '3', 'type': 'Zeze', 'atk_power': '300', 'def_power': '10', 'hp': '100'}, {'id': '4', 'type': 'Zuko', 'atk_power': '100', 'def_power': '25', 'hp': '800'}, {'id': '5', 'type': 'Chacha', 'atk_power': '80', 'def_power': '30', 'hp': '7006'}]
user = [{'id': '1', 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin', 'oc': '0'}, {'id': '2', 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent', 'oc': '9999'}, {'id': '3', 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent', 'oc': '0'}, {'id': '4', 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent', 'oc': '1337'}, {'id': '5', 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent', 'oc': '6699'}]


# REALISASI FUNGSI LAIN
def ui_arena(result:str,oc_received:int, stage:int,damage_dealt:int,damage_received:int):
    def ui_stats(result:str,oc_received:int, stage:int,damage_dealt:int,damage_received:int):
        if not(result == "menang"):
            stage -= 1
        print(f"""============== STATS ==============
Total hadiah      : {oc_received} OC
Jumlah stage      : {stage}
Damage diberikan  : {damage_dealt}
Damage diterima   : {damage_received}
""")
    if result == "menang":
        print(f"""STAGE CLEARED! Anda akan mendapatkan {oc_received} OC pada sesi ini!
              """)
        if stage == 5:
            print("""Selamat, Anda berhasil menyelesaikan seluruh stage Arena !!!
            """)
            ui_stats(result,oc_received,stage,damage_dealt,damage_received)
        else:
            print(f"""Memulai stage berikutnya...
                """)
    elif result == "kalah":
        print(f"""GAME OVER! Sesi latihan berakhir pada stage {stage}!
""")
        ui_stats(result,oc_received,stage,damage_dealt,damage_received)
    else: #result == 'quit'
        ui_stats(result,oc_received,stage,damage_dealt,damage_received)

def select_monster_arena (id: int, user: list[dict],list_monster_user):
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

RAWRRR, Agent {battle.name_user(id,user)} mengeluarkan monster {monster_n(pilihan-1)['type']} !!!

Name : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}""")
    return pilihan,list_player_monster,max_hp_player,base_hp_player
# ///////////////////////////////////////////////////////////////////////////////////////////////////////

def battle_arena(id,user,item_inventory,monster_inventory,monster_dict,level: int,pilihan:int,list_player_monster:list[int],max_hp_player:int,base_hp_player:int): # fungsi utama
    # level = 0 berarti random dan fitur battle saja
    random_num = lcg.randint1(0,len(monster_dict)-1)
    type_monster = monster_dict[random_num]
    if level == 0:
        level_monster = lcg.randint1(1,5)
    else:
        level_monster = level

    skill_monster_enemy = monster.atribut(type_monster,level_monster)
    list_monster_user = battle.user_id_monster(monster_inventory,id)

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
""")
    # variabel untuk damage dealt dan received
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
                print(f"""
Selamat, Anda berhasil mengalahkan monster {type_monster['type']} !!!
                          """)
                result = "menang"
                damage_dealt = hp_enemy
                damage_received = hp_user - list_player_monster[2]
                return(result,damage_dealt,damage_received)
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
                    print(f"""
Yahhh, Anda dikalahkan monster {type_monster['type']}. Jangan menyerah, coba lagi !!!
                          """)
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
                    print(f"""
Yahhh, Anda dikalahkan monster {type_monster['type']}. Jangan menyerah, coba lagi !!!
                          """)
                    result = "kalah"
                    damage_dealt = hp_enemy - skill_monster_enemy[2]
                    damage_received = hp_user
                    return(result,damage_dealt,damage_received)
                    break
                else:
                    turn_num += 1
        
        elif pilihan_2 == 3:
            print("""
GAME OVER! Anda mengakhiri sesi latihan!
                  """)
            result = "quit"
            damage_dealt = hp_enemy - skill_monster_enemy[2]
            damage_received = hp_user - list_player_monster[2]
            return(result,damage_dealt,damage_received)
        else:
            print("""
Maaf input yang anda masukkan tidak ada di pilihan.""")
            break
# PROGRAM UTAMA
def arena (user_id:int, user_data: list[dict], item_inventory: list[dict], monster_inventory: list[dict], monster : list[dict]):
    print("""
    Selamat datang di Arena!!
""")
    list_monster_user = battle.user_id_monster(monster_inventory,user_id)
    pilihan,list_player_monster,max_hp_player,base_hp_player = select_monster_arena(user_id,user_data,list_monster_user)

    stage = 1
    damage_dealt = 0
    damage_received = 0
    oc_received = [0,20,50,90,140,200]
    while True and stage <= 5:
        print(f"""
============= STAGE {stage} =============""")
        result,dmg_dealt,dmg_received = battle_arena(user_id,user_data,item_inventory,monster_inventory,monster,stage,pilihan,list_player_monster,max_hp_player,base_hp_player) 
        damage_dealt += dmg_dealt
        damage_received += dmg_received
        if result == "menang":
            ui_arena(result,oc_received[stage],stage,damage_dealt,damage_received)
            stage +=1
            list_player_monster[2] = max_hp_player
        elif result =="kalah": 
            ui_arena(result,oc_received[stage-1],stage,damage_dealt,damage_received)
            return oc_received[stage-1]
            break
        else: #result == 'quit'
            ui_arena(result,oc_received[stage-1],stage,damage_dealt,damage_received)
            return oc_received[stage-1]
            break
    return oc_received[stage-1]
            
# TESTING
# print(arena('3',user,item_inventory,monster_inventory,monster_dict))

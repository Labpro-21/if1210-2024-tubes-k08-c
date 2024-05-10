import lcg
import load
import os
import monster
import tabel

def user_id_monster(monster_player,id): # fungsi untuk mengambil monster bergantung pada user_id
    list_monster = []
    for i in monster_player:
        if i["user_id"] == str(id):
            list_monster.append(i)

    return list_monster

def add_oc(id,add):
    file_path = os.path.join("data/","init/","user.csv")
    user = load.csv_to_dict(file_path)
    for i in user:
        if i['id'] == str(id):
            i['oc'] = str(int(i['oc']) + add)
            break
    
    tabel.dict_to_csv(file_path,user)

def name_user(id):
    file_path = os.path.join("data/","init/","user.csv")
    user = load.csv_to_dict(file_path)
    for i in user:
        if i['id'] == str(id):
            return i['username']

def battle(id):
    monster_player = load.csv_to_dict(os.path.join("data/","init/","monster_inventory.csv"))
    monster_dict = load.csv_to_dict(os.path.join("data/","init/","monster.csv"))
    random_num = lcg.randint1(0,len(monster_dict)-1)
    type_monster = monster_dict[random_num]
    level_monster = lcg.randint1(1,5)
    skill_monster_enemy = monster.atribut(type_monster,level_monster)
    list_monster_user = user_id_monster(monster_player,id)

    def monster_n(n):
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

RAWRRR, Agent {name_user(id)} mengeluarkan monster {monster_n(pilihan-1)['type']} !!!

Name : {monster_n(pilihan-1)['type']}
ATK Power : {list_player_monster[0]}
DEF Power : {list_player_monster[1]}
HP        : {list_player_monster[2]}
Level     : {list_monster_user[pilihan-1]['level']}
""")

    turn_num = 1
    while True:
        print(f"""============ TURN {turn_num} {monster_n(pilihan-1)['type']} ============
              
1. Attack
2. Use Potion
3. Quit
""")
            
        pilihan_2 = int(input("Pilih perintah: "))
        if pilihan_2 == 1:
            monster.attack(skill_monster_enemy,int(list_player_monster[0]))

            if skill_monster_enemy[2] <= 0:
                skill_monster_enemy[2] = 0
            
            print(f"""\n{monster_n(pilihan-1)['type']},  menyerang {type_monster['type']} !!!

Name      : {type_monster['type']}
ATK Power : {skill_monster_enemy[0]}
DEF Power : {skill_monster_enemy[1]}
HP        : {skill_monster_enemy[2]}
Level     : {level_monster}
""")
            if skill_monster_enemy[2] <= 0:
                print(f"Selamat, Anda berhasil mengalahkan monster {type_monster['type']} !!!")
                add_oc_coin = lcg.randint1(5*level_monster,30*level_monster)
                add_oc(id,add_oc_coin)
                print(f"Total OC yang diperoleh: {add_oc_coin}")
                break
            else:
                monster.attack(list_player_monster,skill_monster_enemy[0])
                if list_player_monster[2] <= 0:
                    list_player_monster[2] = 0
                print(f"""SCHWINKKK, {type_monster['type']} menyerang {monster_n(pilihan-1)['type']} !!!

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
            # fungsi pada potion
            pass
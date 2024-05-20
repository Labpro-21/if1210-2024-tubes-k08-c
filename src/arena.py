import battle
import monster
import potion
import lcg




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

# PROGRAM UTAMA
def arena (user_id:int, user_data: list[dict], item_inventory: list[dict], monster_inventory: list[dict], monster : list[dict]):
    print("""
    Selamat datang di Arena!!
""")
    list_monster_user = battle.user_id_monster(monster_inventory,user_id)
    pilihan,list_player_monster,max_hp_player,base_hp_player = battle.select_monster(user_id,user_data,list_monster_user,monster)

    stage = 1
    damage_dealt = 0
    damage_received = 0
    oc_received = [0,20,50,90,140,200]
    while True and stage <= 5:
        print(f"""
============= STAGE {stage} =============""")
        result,dmg_dealt,dmg_received = battle.battle(user_id,user_data,item_inventory,monster_inventory,monster,stage,pilihan,list_player_monster,max_hp_player,base_hp_player) 
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

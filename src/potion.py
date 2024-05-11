import load
import tabel
import os

csv = [{'user_id': '2', 'type': 'strength', 'quantity': '5'},
       {'user_id': '2', 'type': 'resilience', 'quantity': '3'},
       {'user_id': '3', 'type': 'resilience', 'quantity': '7'},
       {'user_id': '4', 'type': 'healing', 'quantity': '3'},
       {'user_id': '5', 'type': 'strength', 'quantity': '20'}]

def user_id_potion(potion_inventory,id): # fungsi untuk mengambil potion bergantung pada user_id
    list_potion = []
    for i in potion_inventory:
        if i["user_id"] == id:
            list_potion.append(i)

    return list_potion

def up_ability(monster_status,base_hp,max_hp,up):
    if up == 1:
        monster_status[0] = (monster_status[0]*105)//100
    elif up == 2:
        monster_status[1] = (monster_status[1]*105)//100
    elif up == 3:
        monster_status[2] += (base_hp*25)//100
        if monster_status[2] >= max_hp:
            monster_status[2] = max_hp

def potion_in_dict(user_potion):
    list_potion = []
    for i in user_potion:
        list_potion.append(i['type'])

    return list_potion

def find_index(csv,user_id,type):
    index = 0
    for i in csv:
        if i['user_id'] == str(user_id) and i['type'] == type:
            return index
        index += 1

def ui_potion(potion_inventory,monster_name,monster_status,base_hp,max_hp,id,num_potion):
    while True:
        user_potion = user_id_potion(potion_inventory,id)
        dict_potion = {'strength' : 0,
                    'resilience' : 0,
                    'healing' : 0}
        
        for i in user_potion:
            dict_potion[i['type']] = int(i['quantity'])

        print(f"""
============ POTION LIST ============
1. Strength Potion (Qty: {dict_potion['strength']}) - Increases ATK Power
2. Resilience Potion (Qty: {dict_potion['resilience']}) - Increases DEF Power
3. Healing Potion (Qty: {dict_potion['healing']}) - Restores Health
4. Cancel
""")
        pilihan_3 = input("Pilih perintah: ")
        if pilihan_3 == '1':
            if dict_potion['strength'] == 0:
                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
            elif num_potion[0] >= 1:
                print(f"Kamu mencoba memberikan ramuan ini kepada {monster_name}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            else:
                num_potion[0] += 1
                up_ability(monster_status,base_hp,max_hp,int(pilihan_3))
                potion_inventory[find_index(potion_inventory,id,'strength')]['quantity'] = str(int(potion_inventory[find_index(potion_inventory,str(id),'strength')]['quantity']) - 1)
                print(f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {monster_name} dan gerakannya menjadi lebih cepat dan mematikan.")
                aktivate = True
                return aktivate

        elif pilihan_3 == '2':
            if dict_potion['resilience'] == 0:
                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
            elif num_potion[1] >= 1:
                print(f"Kamu mencoba memberikan ramuan ini kepada {monster_name}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            else:
                num_potion[1] += 1
                up_ability(monster_status,base_hp,max_hp,int(pilihan_3))
                potion_inventory[find_index(potion_inventory,id,'resilience')]['quantity'] = str(int(potion_inventory[find_index(potion_inventory,str(id),'resilience')]['quantity']) - 1)
                print(f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {monster_name} yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                aktivate = True
                return aktivate

        elif pilihan_3 == '3':
            if dict_potion['healing'] == 0:
                print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
            elif num_potion[2] >= 1:
                print(f"Kamu mencoba memberikan ramuan ini kepada {monster_name}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
            else:
                num_potion[2] += 1
                up_ability(monster_status,base_hp,max_hp,int(pilihan_3))
                potion_inventory[find_index(potion_inventory,id,'healing')]['quantity'] = str(int(potion_inventory[find_index(potion_inventory,str(id),'healing')]['quantity']) - 1)
                print(f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {monster_name} sembuh dengan cepat. Dalam sekejap, {monster_name} terlihat kembali prima dan siap melanjutkan pertempuran.")
                aktivate = True
                return aktivate

        elif pilihan_3 == '4':
            aktivate = False
            return aktivate

        else:
            print("Perintah tidak ada di dalam pilihan")
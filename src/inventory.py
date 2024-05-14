user_data = [{'id': '1', 'username': 'Mr_Monogram', 'password': 'monogrammer77', 'role': 'admin', 'oc': '0'}, {'id': '2', 'username': 'Asep_Spakbor', 'password': 'asepwow123', 'role': 'agent', 'oc': '9999'}, {'id': '3', 'username': 'Agen_P', 'password': 'platypus123', 'role': 'agent', 'oc': '0'}, {'id': '4', 'username': 'B4ngk1dd0ssss', 'password': 'bangkitganteng', 'role': 'agent', 'oc': '1337'}, {'id': '5', 'username': 'Kenny_agen_rahasia', 'password': 'kribogeming55', 'role': 'agent', 'oc': '6699'}]

monster_data = [{'id': '1', 'type': 'Pikachow', 'atk_power': '125', 'def_power': '10', 'hp': '600'}, {'id': '2', 'type': 'Bulbu', 'atk_power': '50', 'def_power': '50', 'hp': '1200'}, {'id': '3', 'type': 'Zeze', 'atk_power': '300', 'def_power': '10', 'hp': '100'}, {'id': '4', 'type': 'Zuko', 'atk_power': '100', 'def_power': '25', 'hp': '800'}, {'id': '5', 'type': 'Chacha', 'atk_power': '80', 'def_power': '30', 'hp': '7006'}]

inv_item_data = [{'user_id': '2', 'type': 'strength', 'quantity': '5'}, {'user_id': '2', 'type': 'resilience', 'quantity': '3'}, {'user_id': '3', 'type': 'resilience', 'quantity': '7'}, {'user_id': '4', 'type': 'healing', 'quantity': '3'}, {'user_id': '5', 'type': 'strength', 'quantity': '20'}]

inv_monster_data = [{'user_id': '2', 'monster_id': '1', 'level': '1'}, {'user_id': '3', 'monster_id': '2', 'level': '2'}, {'user_id': '3', 'monster_id': '3', 'level': '1'}, {'user_id': '4', 'monster_id': '4', 'level': '1'}, {'user_id': '5', 
'monster_id': '5', 'level': '5'}]

def ext_dict (data: dict, keys_other: list[str]) -> dict:
    row_dict={}
    for j in keys_other:
        row_dict[j] = data[j]
    # li_dict=[]
    # for i in range(len(data)):
    #     row_dict={}
    #     if int(data[i][keys_id]) == id:
    #         for j in keys_other:
    #             row_dict[j] = data[i][j]
    #         li_dict.append(row_dict)
    return row_dict


def oc (user_id: int, user: list[dict]) -> int:
    oc = 0
    for i in range(len(user)):
        if int(user[i]['id']) == user_id:
            oc = user[i]['oc']
            break
    return oc

def item_inv (user_id: int, item_inventory:list[dict]) -> list[dict]:
    item = []
    for i in range(len(item_inventory)):
        if int(item_inventory[i]['user_id']) == user_id:
            item.append(ext_dict(item_inventory[i],['type','quantity']))
    return item

def monster_inv (user_id : int, monster_inventory: list[dict], monster: list[dict]) -> list[dict]: #memperoleh monster yang dipunyai user
    monster_id = []
    monster_level = []
    for i in range(len(monster_inventory)):
        if user_id == int(monster_inventory[i]['user_id']):
            monster_id.append(int(monster_inventory[i]['monster_id']))
            monster_level.append(int(monster_inventory[i]['level']))
    if len(monster_id)>0:
        inv_monster = []
        for i in range(len(monster_id)):
            for j in range(len(monster)):
                if monster_id[i] == int(monster[j]['id']):
                    inv_monster.append(ext_dict(monster[j],['type','atk_power','def_power','hp']))
        for i in range(len(monster_level)):
            inv_monster[i]['level'] = monster_level[i]
    else:
        inv_monster = []
    return inv_monster

def ui_main_inventory(user_id:int,oc:int,item:list[dict],monster:list[dict]):
    print(f"""
============ INVENTORY LIST (User ID: {user_id}) ============
Jumlah O.W.C.A. Coin-mu sekarang {oc}.""")
    number = 0
    for i in range(len(monster)):
        number +=1
        print(f"{number}. Monster       (Name: {monster[i]['type']}, Lvl: {monster[i]['level']}, HP: {monster[i]['hp']})")
    for i in range(len(item)):
        number +=1
        print(f"{number}. Potion        (Type: {item[i]['type']}, Qty: {item[i]["quantity"]})")
    print()

def ui_monster_inventory(monster:dict):
    print(f"""
Monster
Name      : {monster['type']}
ATK Power : {monster['atk_power']}
DEF Power : {monster['def_power']}
HP        : {monster['hp']}
Level     : {monster['level']} 
""")

def ui_item_inventory (item:dict):
    print(f"""
Potion
Type      : {item['type']}
Quantity  : {item['quantity']} 
""")

def inventory (user_id:int,user:list[dict],item_inventory:list[dict],monster_inventory:list[dict],monster:list[dict]):
    user_oc = oc(user_id,user)
    user_item = item_inv(user_id,item_inventory)
    user_monster = monster_inv(user_id,monster_inventory,monster)
    ui_main_inventory(user_id,user_oc,user_item,user_monster)
    print("Ketikkan id untuk menampilkan detail item:")
    id_input = (input(">>> "))
    print()
    while not(id_input == "KELUAR"):
        if id_input == "INV":
            ui_main_inventory(user_id,user_oc,user_item,user_monster)
        elif int(id_input) > len(user_monster)+len(user_item) or int(id_input) <= 0:
            print("Maaf id yang dimasukkan tidak ada dipilihan.")
        elif int(id_input) > len(user_monster):
            ui_item_inventory(user_item[(int(id_input)-len(user_monster))-1])
        else: 
            ui_monster_inventory(user_monster[int(id_input)-1])
        print("Ketikkan id untuk menampilkan detail item:")
        id_input = (input(">>> "))
        print()
    return {'oc': user_oc, 'potion':user_item,'monster': user_monster}    

print(inventory(5,user_data,inv_item_data,inv_monster_data,monster_data))
def list_dict (id: int, data: list[dict], keys_id: str, keys_other: list[str]) -> list[dict]:
    li_dict=[]
    for i in range(len(data)):
        row_dict={}
        if data[i][keys_id] == id:
            for j in keys_other:
                row_dict[j] = data[i][j]
            li_dict.append(row_dict)
    return li_dict


def oc (user_id: int, user: list[dict]) -> int:
    oc = 0
    for i in range(len(user)):
        if user[i]['id'] == user_id:
            oc = user[i]['oc']
    return oc

def item_inv (user_id: int, item_inventory:list[dict]) -> list[dict]:
    item = list_dict(user_id, item_inventory, 'user_id',['type','quantity'])
    return item

def monster_inv (user_id : int, monster_inventory: list[dict], monster: list[dict]) -> list[dict]: #memperoleh monster yang dipunyai user
    monster_id = []
    monster_level = []
    for i in range(len(monster_inventory)):
        if user_id == monster_inventory[i]['user_id']:
            monster_id.append(monster_inventory[i]['monster_id'])
            monster_level.append(monster_inventory[i]['level'])
    inv_monster = []
    for id in monster_id:
        inv_monster.append(list_dict(id,monster,'id',['type','atk_power','def_power','hp']))
    for i in range(len(monster_level)):
        inv_monster[i]['level'] = monster_level[i]
    return inv_monster

def ui_main_inventory(oc:int,item:list[dict],monster:list[dict]):
    print(f"""
============ INVENTORY LIST (User ID: 1) ============
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
    ui_main_inventory(user_oc,user_item,user_monster)
    print("Ketikkan id untuk menampilkan detail item:")
    id_input = int(input(">>> "))
    while not(id_input == "KELUAR"):
        if id_input > len(user_monster):
            ui_item_inventory(user_item[(id_input-len(user_monster))-1])
        else: 
            ui_monster_inventory(user_monster[id_input-1])
        print("Ketikkan id untuk menampilkan detail item:")
        id_input = int(input(">>> "))
    return {'oc': user_oc, 'potion':user_item,'monster': user_monster}    
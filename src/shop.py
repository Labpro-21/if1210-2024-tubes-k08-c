# import src.load as load . tlg langsung parameter fungsi
import tabel as tabulasi

# fungsi untuk mengecek keberadaan suatu elemen dalam list of dictionaries
def exist(list_of_dict,n,category):
    for i in range(len(list_of_dict)):
        if list_of_dict[i][category] == n:
            return True
    return False

# fungsi untuk mengembalikan indeks dari suatu elemen yang dicari dalam list of dictionaries
def index(list_of_dict,n,category):
    for i in range(len(list_of_dict)):
        if list_of_dict[i][category] == n:
            return i

# fungsi untuk membuat textbox (hiasan)
def textbox(text):
    print("╔" + "═"*(len(text)+2) + "╗")
    print("║" + " " + text + " " + "║")
    print("╚" + "═"*(len(text)+2) + "╝")

def user_id_monster(monster_inventory : list[dict[int]], user_id: int) -> list[dict[int]]: # fungsi untuk mengambil monster bergantung pada user_id
    list_monster = []
    for i in monster_inventory:
        if i['user_id'] == user_id:
            list_monster.append(i)
    return list_monster

# fungsi untuk membuka shop khusus transaksi monster
def monster_shop(monster_data,shop_monster_data,inv_monster_data,users_data,user_id):
    textbox("Imported directly from ragunan! type the [ID] to choose your desired monster and type [back] to get back to main shop")
    print()
    while True:
        display_monster_shop = []
        for i in range(len(shop_monster_data)):
            if exist(monster_data,shop_monster_data[i]['monster_id'],"id"):
                display_monster_shop.append(monster_data[index(monster_data,shop_monster_data[i]['monster_id'],"id")])
            display_monster_shop[i]['stock'] = shop_monster_data[i]['stock']
            display_monster_shop[i]['price'] = shop_monster_data[i]['price']
            user_id_monster_list = user_id_monster(inv_monster_data,user_id)
        print(display_monster_shop)
        tabulasi.tabel(display_monster_shop,['ID','Type','ATK Power','DEF Power','HP','Stock','Price'])
        buy = input("➤ ")
        if buy.upper() == "BACK":
            break
        elif exist(shop_monster_data,int(buy),'monster_id'):
            if not exist(user_id_monster_list,buy,'monster_id'):
                while True:
                    if int(display_monster_shop[index(display_monster_shop,int(buy),"id")]['stock']) < 1:
                        textbox(f"it seems that i ran out of stock on that monster, please choose something else")
                        break
                    else:
                        if int(users_data[index(users_data,user_id,'id')]["oc"]) >= int(shop_monster_data[index(shop_monster_data,int(buy),'monster_id')]['price']):
                            while True:
                                textbox(f"you currently have {users_data[index(users_data,user_id,'id')]["oc"]} oc and the price is {shop_monster_data[index(shop_monster_data,int(buy),'monster_id')]['price']} oc, are you sure you want to buy this? [y/n]")
                                confirm = input("➤ ")
                                if confirm.upper() == "Y":
                                    inv_monster_data.append({'user_id':user_id,'monster_id':buy,'level':'1'})
                                    shop_monster_data[index(shop_monster_data,int(buy),'monster_id')]['stock'] = str(int(shop_monster_data[index(shop_monster_data,int(buy),'monster_id')]['stock']) - 1)
                                    users_data[index(users_data,user_id,'id')]["oc"] = str(int(users_data[index(users_data,user_id,'id')]["oc"]) - int(shop_monster_data[index(shop_monster_data,int(buy),'monster_id')]['price']))
                                    textbox(f"thank you for your patronage! you currently have {users_data[index(users_data,user_id,'id')]["oc"]} oc left in your wallet")
                                    break
                                elif confirm.upper() == "N":
                                    break
                        else:
                            textbox(f"you only have {users_data[index(users_data,user_id,'id')]["oc"]} oc lmao, come back when you have the money")
                            break
                    break
            else:
                textbox("nuh uh...it seems that you already have that monster")
        else:
            textbox("let me repeat myself, choose one of the monster i have by typing the [ID] of the monster or get back to the main shop by typing [back]")

# fungsi untuk membuka shop khusus transaksi item
def item_shop(inv_item_data,shop_item_data,users_data,user_id):
    textbox("Best to supply your journey! Type the [item_id] to choose your desired potion and type [back] to get back to main shop")
    print()
    while True:
        display_item_shop = []
        for i in range(len(shop_item_data)):
            item = {'item_id': str(i + 1), 'type': shop_item_data[i]['type'], 'stock': shop_item_data[i]['stock'], 'price': shop_item_data[i]['price']}
            display_item_shop.append(item)
        tabulasi.tabel(display_item_shop,['Item Id','Type','Stock','Price'])
        print("")
        buy = input("➤ ")
        if buy.upper() == "BACK":
            break
        elif exist(display_item_shop,buy,'item_id'):
            textbox("how many of that item you want dear customer?")
            while True:
                qty = int(input("➤ "))
                if qty <= int(display_item_shop[int(buy)-1]['stock']):
                    break
                else:
                    textbox(f"it seems that i only have {display_item_shop[int(buy)-1]['stock']} of them. please lower your demand")
                    break
            if int(users_data[index(users_data,user_id,'id')]["oc"]) >= int(display_item_shop[int(buy)-1]['price'])*qty:
                    while True:
                        textbox(f"you currently have {users_data[index(users_data,user_id,'id')]["oc"]} oc and the price is {int(display_item_shop[int(buy)-1]['price'])*qty} oc, are you sure you want to buy this? y/n")
                        confirm = input("➤ ")
                        if confirm.upper() == "Y":
                            include = False
                            for i in range(len(inv_item_data)):
                                if (inv_item_data[i]['user_id'] == user_id) and (inv_item_data[i]['type'] == display_item_shop[int(buy)-1]['type']):
                                    inv_item_data[i]['quantity'] = str(int(inv_item_data[i]['quantity']) + 1)
                                    include = True
                            if not include:
                                inv_item_data.append({"user_id": user_id,"type":display_item_shop[int(buy)-1]['type'],"quantity":1})
                            shop_item_data[int(buy)-1]["stock"] = str(int(shop_item_data[int(buy)-1]["stock"]) - qty)
                            users_data[index(users_data,user_id,'id')]["oc"] = str(int(users_data[index(users_data,user_id,'id')]["oc"]) - int(shop_item_data[int(buy)-1]['price'])*qty)
                            textbox(f"thank you for your patronage! you currently have {users_data[index(users_data,user_id,'id')]["oc"]} oc left in your wallet")
                            break
                        elif confirm.upper() == "N":
                            break
            else:
                textbox(f"you only have {users_data[index(users_data,user_id,'id')]["oc"]} oc lmao, come back when you have the money")
        else:
            textbox("let me repeat myself, choose one of the monster i have by typing the [ID] of the monster or get back to the main shop by typing [back]")

# fungsi general shop yang akan dipanggil di main
def shop(shop_monster_data,monster_data,inv_monster_data,shop_item_data,inv_item_data,users_data,user_id):
    # inisiasi list of dictionaries baru untuk di-display di monster shop
    npc = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠤⠤⠤⠒⠒⠒⠒⠒⠒⠒⠒⠒⠂⠦⠤⠤⠄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠉⠀⣀⣀⠤⠤⠖⠒⠒⠒⠈⠉⠉⠉⠁⠒⠒⠢⠤⢄⣀⠀⠉⠑⠢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠴⠊⠁⣀⡤⠖⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠢⢄⡀⠈⠓⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⢁⡠⠖⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⢄⠀⠉⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠞⣡⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠢⣄⠈⠣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠎⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⡰⢋⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢢⠘⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡜⢁⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⢣⡘⣆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡞⢀⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⣤⠀⠀⠈⡏⢣⠀⢳⡈⣆⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡞⢀⡎⠀⠀⡴⠋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡀⢸⠹⡄⠀⠈⢧⠀⠀⢱⠘⡆⠀⢣⠘⡄⠀⠀⠀⠀
⠀⠀⠀⠀⡼⠀⡜⠀⠀⠸⠀⢰⠃⠀⠀⠀⡴⢲⠀⠀⠀⠀⠀⠿⡄⠀⠀⠀⢀⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⢧⠇⠀⠀⠘⡆⠀⠀⠳⠇⠀⠈⡆⢳⠀⠀⠀⠀
⠀⠀⠀⣼⠃⢰⠁⠀⠀⢠⣠⠏⠀⠀⠀⠀⣅⡼⠀⠀⠀⠀⠀⣠⠃⠀⠀⠀⡜⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⠉⠀⠈⠃⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⢹⠈⡇⠀⠀⠀
⠀⢀⡞⡏⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⢰⠇⠀⠀⢸⡀⠀⠀⠀⠀⡆⠀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠈⡆⠃⠀⠀⠀
⢠⠎⢠⠁⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⠀⠀⠀⠀⢧⠀⠀⠀⠀⣷⠀⠀⠀⠀⠈⡇⠀⠀⢀⠀⠀⠀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀
⠃⠀⢸⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⡇⠀⠀⠀⠀⠘⡆⠀⠀⢠⣽⣧⣄⣀⣀⠀⢹⡀⠀⢸⡀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⢧⢸⠀⠀⠀
⠀⠀⡈⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢩⡀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⢹⡄⠀⠀⢸⡘⣆⠀⠀⠀⠘⣷⠀⠀⡇⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠘⣆⢣⡀⠀
⠀⠀⡇⢀⡿⡇⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⡇⠘⡄⠀⠀⠀⢯⢣⡀⣇⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠈⠢⣙⠢
⠀⠀⢧⢸⠀⣇⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠀⠀⠀⠀⢹⢳⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⢷⠀⠹⡄⠀⠀⢸⠀⢳⣻⠀⠀⠀⠀⠀⠀⢿⡀⠀⠀⠀⠀⠀⠀⠀⠈⠑
⠀⠀⢸⢸⠀⢸⡀⠀⠀⢠⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⢸⠸⡄⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠳⡄⢸⠀⠀⠙⡄⠀⠘⡇⠀⢹⠀⠀⠀⠀⠀⠀⠸⠻⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣼⠀⣸⢧⠀⠀⠸⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣸⣀⣇⣀⣀⣀⡸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣀⣙⣼⣀⣀⣀⣘⣦⣀⣇⣀⢸⠀⡄⠀⠀⠀⠀⠸⠀⣟⢦⡀⠀⠀⠀⢰⣦⠀
⠀⠀⠀⢹⣴⡇⠈⢧⠀⠀⡄⠀⠀⠀⢠⡐⠛⣿⠛⠛⢻⣿⣿⣛⢛⣟⣳⡇⠀⠀⠀⠀⠀⠀⠀⠐⣻⣿⠿⠿⠿⠿⢿⣿⣿⠟⠓⢺⠀⡇⠀⠀⠀⠀⢸⣸⡇⠀⢷⠀⠀⠀⡏⠸⡄
⠀⠀⢠⣞⡵⢻⡀⠈⣳⡀⡇⠀⠀⠀⠸⠷⡶⠿⠶⢖⣚⣉⠉⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢿⣋⣉⣉⣉⣙⠿⠋⡀⠀⡜⠀⡇⠀⠀⠀⠀⢸⡿⠀⠀⢸⠀⢀⠜⠀⠀⡇
⠀⠀⠀⠀⠀⠀⠑⢤⡏⠻⣇⠀⢀⡠⠔⠊⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠀⡇⢸⠇⠀⠀⠀⠀⣸⣤⠀⠀⢸⠴⠃⠀⠀⢰⡔
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⡿⠋⣁⡤⠖⠋⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⢁⣿⠀⠀⣀⡤⡤⠟⣛⡠⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠋⠁⠀⣀⡤⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣧⢿⣿⠞⠉⠁⠀⠀⠀⠃⠀⠠⠄⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡤⠖⠋⣡⠔⠛⢳⠦⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⡶⠟⠋⢹⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡤⠖⠋⠀⠀⠀⣸⠀⠈⢦⣿⠙⠳⣶⡠⠤⣤⣤⣀⡀⠀⢀⣠⠤⠀⣴⣶⣶⣿⢿⣿⣿⣷⣴⣷⣹⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢀⡄⠀⣠⠞⠁⠀⠀⠀⠛⠀⠀⢀⣽⣿⣿⡏⢹⢿⣿⡅⠀⠀⢠⡿⣿⣿⡏⠀⣿⡿⠟⢻⣷⣿⡚⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⢸⠻⠚⠁⠀⠀⠀⠀⠀⠀⢀⡔⠛⠻⠿⣿⡄⢀⡟⠛⣿⣆⣠⠟⠀⠛⣷⡁⠀⣱⣧⠴⠛⠋⠉⠉⢳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⠋⠀⠀⠀⠀⠀⠀⠀⠀⢀⡎⠀⠀⠀⠀⠈⢻⣼⠃⠀⠀⠙⠋⠀⠀⠀⠀⠳⣼⠋⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⢀⣿⠓⠲⠤⠤⠤⠽⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠤⠤⠤⠤⠤⢴⡆⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠈⡆⠀⠀⠀⠀⠀⠀

╔══════════════════╗
║ Ryo the Merchant ║
╚══════════════════╝
"""
    while True:
        print(npc,end="")
        textbox("Watcha buyin? Are you in the mood for [monster/item]? Or... you can also leave by typing [exit]")
        choice = input("➤ ")
        if choice.upper() == "EXIT": 
            break
        elif choice.upper() == "MONSTER":
            monster_shop(monster_data,shop_monster_data,inv_monster_data,users_data,user_id)
        elif choice.upper() == "ITEM":
            item_shop(inv_item_data,shop_item_data,users_data,user_id)
        else:
            textbox("we don't sell that here")

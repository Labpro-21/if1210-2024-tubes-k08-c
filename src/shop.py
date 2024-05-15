import src.load as load
import src.tabel as tabulasi
import src.additionals.code_functions as code
import src.additionals.design_functions as design

users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()

# inisiasi list of dictionaries baru untuk di-display di monster shop
display_monster_shop = []
for i in range(len(shop_monster_data)):
    if code.exist(monster_data,shop_monster_data[i]['monster_id'],"id"):
        display_monster_shop.append(monster_data[code.index(monster_data,shop_monster_data[i]['monster_id'],"id")])
    display_monster_shop[i]['stock'] = shop_monster_data[i]['stock']
    display_monster_shop[i]['price'] = shop_monster_data[i]['price']

# inisiasi list of dictionaries baru untuk didisplay di item shop
display_item_shop = []
for i in range(len(shop_item_data)):
    item = {'item_id': str(i + 1), 'type': shop_item_data[i]['type'], 'stock': shop_item_data[i]['stock'], 'price': shop_item_data[i]['price']}
    display_item_shop.append(item)

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

# fungsi untuk membuka shop khusus transaksi monster
def monster_shop():
    design.textbox("Imported directly from ragunan! Choose the one that suits you the most!")
    print()
    design.textbox("*type the monster_id to choose your desired monster and type 'back' to get back to main shop")
    print()
    while True:
        tabulasi.tabel(display_monster_shop,['id','type','atk_power','def_power','hp','stock','price'])
        buy = input("➤ ")
        if buy.upper() == "BACK":
            break
        elif code.exist(shop_monster_data,buy,'monster_id'):
            if not code.exist(inv_monster_data,buy,'monster_id'):
                if int(users_data[code.index(users_data,id,'id')]["oc"]) >= int(shop_monster_data[code.index(shop_monster_data,buy,'monster_id')]['price']):
                    while True:
                        design.textbox(f"you currently have {users_data[code.index(users_data,id,'id')]["oc"]}. Are you sure you want to buy this? y/n")
                        confirm = input("➤ ")
                        if confirm.upper() == "Y":
                            inv_monster_data.append(shop_monster_data[code.index(shop_monster_data,buy,'monster_id')])
                            shop_monster_data[code.index(shop_monster_data,buy,'monster_id')]['stock'] = str(int(shop_monster_data[code.index(shop_monster_data,buy,'monster_id')]['stock']) - 1)
                            users_data[code.index(users_data,id,'id')]["oc"] = str(int(users_data[code.index(users_data,id,'id')]["oc"]) - int(shop_monster_data[code.index(shop_monster_data,buy,'monster_id')]['price']))
                            break
                        elif confirm.upper() == "N":
                            break
                else:
                    design.textbox("bruh you don't even have enough money... take a loan and comeback to me later")
            else:
                design.textbox("nuh uh...it seems that you already have that monster")
        else:
            design.textbox("let me repeat myself, choose one of the monster i have by the id number or just get out of my shop")

# fungsi untuk membuka shop khusus transaksi item
def item_shop():
    design.textbox("Best to supply your journey! take one of these cool and awesome items.")
    print()
    design.textbox("*type the item_id to choose your desired potion and type 'back' to get back to main shop")
    print()
    while True:
        tabulasi.tabel(display_item_shop,['item_id','type','stock','price'])
        buy = input("➤ ")
        if buy.upper() == "BACK":
            break
        elif code.exist(display_item_shop,buy,'item_id'):
            design.textbox("how many of that item you want dear customer?")
            while True:
                qty = int(input("➤ "))
                if qty <= int(display_item_shop[int(buy)-1]['stock']):
                    break
                else:
                    print("it seems that i don't have that many items. please lower your demand")
            if int(users_data[code.index(users_data,id,'id')]["oc"]) >= int(display_item_shop[int(buy)-1]['price'])*qty:
                    while True:
                        design.textbox(f"you currently have {users_data[code.index(users_data,id,'id')]["oc"]}. Are you sure you want to buy this? y/n")
                        confirm = input("➤ ")
                        if confirm.upper() == "Y":
                            include = False
                            for i in range(len(inv_item_data)):
                                if (inv_item_data[i]['user_id'] == id) and (inv_item_data[i]['type'] == display_item_shop[int(buy)-1]['type']):
                                    inv_item_data[i]['quantity'] = str(int(inv_item_data[i]['quantity']) + 1)
                                    include = True
                            if not include:
                                inv_item_data.append({"user_id": id,"type":display_item_shop[int(buy)-1]['type'],"quantity":1})
                            shop_item_data[int(buy)-1]["stock"] = str(int(shop_item_data[int(buy)-1]["stock"]) - qty)
                            display_item_shop[int(buy)-1]["stock"] = str(int(display_item_shop[int(buy)-1]["stock"]) - qty)
                            users_data[code.index(users_data,id,'id')]["oc"] = str(int(users_data[code.index(users_data,id,'id')]["oc"]) - int(shop_item_data[int(buy)-1]['price']))
                            break
                        elif confirm.upper() == "N":
                            break
            else:
                design.textbox("bruh you don't even have enough money... take a loan and comeback to me later")
        else:
            design.textbox("let me repeat myself, choose one of the monster i have by the id number or just get out of my shop")

# fungsi general shop yang akan dipanggil di main
def shop():
    while True:
        print(npc,end="")
        design.textbox("Watcha Buyin? Are you in the mood for monster or item?")
        choice = input("➤ ")
        if choice.upper() == "EXIT":
            break
        elif choice.upper() == "MONSTER":
            monster_shop()
        elif choice.upper() == "ITEM":
            item_shop()
        else:
            design.textbox("we don't sell that here")
import tabel as tabulasi


# fungsi untuk mengecek keberadaan suatu elemen dalam list of dictionaries
def exist(list_of_dict, n, category):
    for i in range(len(list_of_dict)):
        if list_of_dict[i][category] == n:
            return True
    return False


# fungsi untuk mengembalikan indeks dari suatu elemen yang dicari dalam list of dictionaries
def index(list_of_dict, n, category):
    for j in range(len(list_of_dict)):
        if list_of_dict[j][category] == n:
            return j


# view option
def view(monster_data: list[dict],
         shop_item_data: list[dict],
         shop_monster_data: list[dict],
         display_monster_shop: list[dict],
         display_item_shop: list[dict]
         ):
    choice = str(input("MONSTER / ITEM: "))
    if choice.lower() == "monster":
        tabulasi.tabel(display_monster_shop, ['ID', 'Type', 'Atk Power', 'Def Power', 'HP', 'Stock', 'Price'])
    elif choice.lower() == "item":
        tabulasi.tabel(display_item_shop, ['Item ID', 'Type', 'Stock', 'Price'])


# add option
def add(monster_data: list[dict],
        shop_item_data: list[dict],
        shop_monster_data: list[dict],
        display_monster_shop: list[dict],
        display_item_shop: list[dict]
        ):
    choice = str(input("MONSTER / ITEM: "))
    if choice.lower() == "monster":
        unsold_mons = []
        for i in range(len(monster_data)):
            if not exist(display_monster_shop, monster_data[i]['id'], "id"):
                unsold_mons.append(monster_data[i])
        if unsold_mons:
            tabulasi.tabel(unsold_mons, ['ID', 'Type', 'Atk Power', 'Def Power', 'HP'])
            monsterid = int(input("Enter Monster ID: "))
            initialstock = input("Enter initial stock: ")
            price = input("Enter price: ")
            shop_monster_data[monsterid - 1]["stock"] = initialstock
            shop_monster_data[monsterid - 1]["price"] = price
            print(f"{monster_data[monsterid - 1]['type']} has been added to shop!")
        else:
            print("All monsters in the database are available for purchase !!!")
    elif choice.lower() == "item":
        unsold_potions = []
        for i in range(len(display_item_shop)):
            if display_item_shop[i]["stock"] == 0:
                unsold_potions.append(display_item_shop[i])
        if unsold_potions:
            tabulasi.tabel(unsold_potions, ["id", "type"])
            itemid = int(input("Enter Item id: "))
            initialstock = input("Enter initial stock: ")
            price = input("Enter price: ")
            shop_item_data[itemid - 1]["stock"] = initialstock
            shop_item_data[itemid - 1]["price"] = price
            print(f"{shop_item_data[itemid - 1]['type']} has been added to shop!")
        else:
            print("All items are available for purchase !!!")
    return shop_item_data, shop_monster_data


# edit option
def edit(monster_data: list[dict],
         shop_item_data: list[dict],
         shop_monster_data: list[dict],
         display_monster_shop: list[dict],
         display_item_shop: list[dict]):
    choice = str(input("MONSTER / ITEM "))
    if choice.lower() == "monster":
        tabulasi.tabel(display_monster_shop, ['ID', 'Type', 'Atk Power', 'Def Power', 'HP', 'Stock', 'Price'])
        monsterid = int(input("Enter Monster ID: "))
        newstock = input("Enter new stock: ")
        newprice = input("Enter new price: ")
        if newstock and not newprice:  # only change stock
            shop_monster_data[monsterid - 1]['stock'] = newstock
            print(f"{monster_data[monsterid - 1]['type']} has been restocked with a quantity of {newstock}!")
        elif newprice and not newstock:  # only change price
            shop_monster_data[monsterid - 1]['price'] = newprice
            print(f"{monster_data[monsterid - 1]['type']} has been updated with a price of {newprice}!")
        elif newstock and newprice:  # change both stock and price
            shop_monster_data[monsterid - 1]['stock'] = newstock
            shop_monster_data[monsterid - 1]['price'] = newprice
            print(
                f"{monster_data[monsterid - 1]['type']} has been restocked with a quantity of {newstock} and has been updated with a price of {newprice}!")
    elif choice.lower() == "item":
        tabulasi.tabel(display_item_shop, ['Item ID', 'Type', 'Stock', 'Price'])
        itemid = int(input("Enter Item id: "))
        newstock = input("Enter new stock: ")
        newprice = input("Enter new price: ")
        if newstock and not newprice:  # only change stock
            shop_item_data[itemid - 1]['stock'] = newstock
            print(f"{shop_item_data[itemid - 1]['type']} has been restocked with a quantity of {newstock}!")
        elif newprice and not newstock:  # only change price
            shop_item_data[itemid - 1]['price'] = newprice
            print(f"{shop_item_data[itemid - 1]['type']} has been updated with a price of {newprice}!")
        elif newstock and newprice:  # change both stock and price
            shop_item_data[itemid - 1]['stock'] = newstock
            shop_item_data[itemid - 1]['price'] = newprice
            print(
                f"{shop_item_data[itemid - 1]['type']} has been restocked with a quantity of {newstock} and has been updated with a price of {newprice}!")
    return shop_item_data, shop_monster_data


# delete option
def delete(monster_data: list[dict],
           shop_item_data: list[dict],
           shop_monster_data: list[dict],
           display_monster_shop: list[dict],
           display_item_shop: list[dict]):
    choice = str(input("MONSTER / ITEM: "))
    if choice.lower() == "monster":
        tabulasi.tabel(display_monster_shop, ['ID', 'Type', 'ATK Power', 'Def Power', 'hp', 'stock', 'price'])
        monsterid = int(input("Enter Monster ID: "))
        yn = str(input(f"Are you sure you want to delete {monster_data[monsterid - 1]['type']} from the shop? (y/n) "))
        if yn.lower() == 'y':
            shop_monster_data[monsterid-1]["stock"] = 0
            print(f"{monster_data[monsterid - 1]['type']} has been deleted from the shop!")
    elif choice.lower() == "item":
        tabulasi.tabel(display_item_shop, ['Item ID', 'Type', 'Stock', 'Price'])
        itemid = int(input("Enter Item id: "))
        yn = str(input(f"Are you sure you want to delete {shop_item_data[itemid - 1]['type']} from the shop? (y/n) "))
        if yn.lower() == 'y':
            shop_item_data[itemid-1]["stock"] = 0
            print(f"{shop_item_data[itemid - 1]['type']} has been deleted from the shop!")
    return shop_item_data, shop_monster_data


# MAIN PROGRAM
def shop_management(
        monster_dat: list[dict],
        shop_item_dat: list[dict],
        shop_monster_dat: list[dict]):
    print(">>> SHOP")
    print("Ah.. it's good to see you again. Welcome!")
    # assume the user's input is always valid
    while True:
        # inisiasi list of dictionaries baru untuk di-display di monster shop
        display_monster = []
        for i in range(len(shop_monster_dat)):
            if exist(monster_dat, shop_monster_dat[i]['monster_id'], "id") and shop_monster_dat[i]['stock'] != 0:
                display_monster.append(monster_dat[i])
                display_monster[i]["stock"] = shop_monster_dat[i]["stock"]
                display_monster[i]["price"] = shop_monster_dat[i]["price"]
                # inisiasi list of dictionaries baru untuk didisplay di item shop
        display_item = []
        for i in range(len(shop_item_dat)):
            if shop_item_dat[i]['stock'] != 0:
                item = {'item_id': str(i + 1), 'type': shop_item_dat[i]['type'], 'stock': shop_item_dat[i]['stock'],
                        'price': shop_item_dat[i]['price']}
                display_item.append(item)
        option = str(input("OPTIONS: VIEW / ADD / EDIT / DELETE / EXIT: "))
        if option.lower() == 'view':
            view(monster_dat, shop_item_dat, shop_monster_dat, display_monster, display_item)
        elif option.lower() == 'add':
            shop_item_dat, shop_monster_dat = add(monster_dat, shop_item_dat, shop_monster_dat, display_monster, display_item)
        elif option.lower() == 'edit':
            shop_item_dat, shop_monster_dat = edit(monster_dat, shop_item_dat, shop_monster_dat, display_monster, display_item)
        elif option.lower() == 'delete':
            shop_item_dat, shop_monster_dat = delete(monster_dat, shop_item_dat, shop_monster_dat, display_monster, display_item)
        elif option.lower() == 'exit':
            print("Alrighty, safe travels! Hope to see you again~")
            break
    return shop_item_dat, shop_monster_dat

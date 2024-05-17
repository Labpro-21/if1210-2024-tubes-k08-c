import src.load as load
import src.save as save
import src.tabel as tabulasi

# data loading
user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()

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

# inisiasi list of dictionaries baru untuk di-display di monster shop
display_monster_shop = []
for i in range(len(shop_monster_data)):
    if exist(monster_data,shop_monster_data[i]['monster_id'],"id"):
        display_monster_shop.append(monster_data[index(monster_data,shop_monster_data[i]['monster_id'],"id")])
    display_monster_shop[i]['stock'] = shop_monster_data[i]['stock']
    display_monster_shop[i]['price'] = shop_monster_data[i]['price']

# inisiasi list of dictionaries baru untuk didisplay di item shop
display_item_shop = []
for i in range(len(shop_item_data)):
    item = {'item_id': str(i + 1), 'type': shop_item_data[i]['type'], 'stock': shop_item_data[i]['stock'], 'price': shop_item_data[i]['price']}
    display_item_shop.append(item)

# view option
def view(): 
    choice = str(input("MONSTER / ITEM "))
    if choice.lower() == "monster":
      tabulasi.tabel(display_monster_shop,['id','type','atk_power','def_power','hp','stock','price'])
    elif choice.lower() == "item":
      tabulasi.tabel(display_item_shop,['item_id','type','stock','price'])

# add option
def add():
    choice = str(input("MONSTER / ITEM "))
    if choice.lower() == "monster":
        show_monster = []
        for i in range(len(shop_monster_data)):
            if shop_monster_data[i]["stock"] == 0:
                show_monster.append(shop_monster_data[i])
                # belom selesai 

# edit option
def edit():
    choice = str(input("MONSTER / ITEM "))
    if choice.lower() == "monster":
        tabulasi.tabel(display_monster_shop,['id','type','atk_power','def_power','hp','stock','price'])
        monsterid = int(input("Enter Monster ID: "))
        newstock = input("Enter new stock: ")
        newprice = input("Enter new price: ")
        if newstock and not newprice: # only change stock
            shop_monster_data[monsterid-1]['stock'] = newstock
            print(f"{monster_data[monsterid-1]['type']} has been restocked with a quantity of {newstock}!")
        elif newprice and not newstock: # only change price
            shop_monster_data[monsterid-1]['price'] = newprice
            print(f"{monster_data[monsterid-1]['type']} has been updated with a price of {newprice}!")
        elif newstock and newprice: # change both stock and price
            shop_monster_data[monsterid-1]['stock'] = newstock
            shop_monster_data[monsterid-1]['price'] = newprice
            print(f"{monster_data[monsterid-1]['type']} has been restocked with a quantity of {newstock} and has been updated with a price of {newprice}!")
    elif choice.lower() == "item":
        tabulasi.tabel(display_item_shop,['item_id','type','stock','price'])
        itemid = int(input("Enter Item (1 for Strength, 2 for Resilience, 3 for Healing): "))
        newstock = input("Enter new stock: ")
        newprice = input("Enter new price: ")
        if newstock and not newprice: # only change stock
            shop_item_data[itemid-1]['stock'] = newstock
            print(f"{shop_item_data[itemid-1]['type']} has been restocked with a quantity of {newstock}!")
        elif newprice and not newstock: # only change price
            shop_item_data[itemid-1]['price'] = newprice
            print(f"{shop_item_data[itemid-1]['type']} has been updated with a price of {newprice}!")
        elif newstock and newprice: # change both stock and price
            shop_item_data[itemid-1]['stock'] = newstock
            shop_item_data[itemid-1]['price'] = newprice
            print(f"{monster_data[itemid-1]['type']} has been restocked with a quantity of {newstock} and has been updated with a price of {newprice}!")

# delete option
def delete():
    choice = str(input("MONSTER / ITEM "))
    if choice.lower() == "monster":
        tabulasi.tabel(display_monster_shop,['id','type','atk_power','def_power','hp','stock','price'])
        monsterid = int(input("Enter Monster ID: "))
        yn = str(input(f"Are you sure you want to delete {monster_data[monsterid-1]['type']} from the shop? (y/n) "))
        if yn.lower() == 'y':
            shop_monster_data[monsterid]["stock"] = 0
            print(f"{monster_data[monsterid-1]['type']} has been deleted from the shop!")
    elif choice.lower() == "item":
        tabulasi.tabel(display_item_shop,['item_id','type','stock','price'])
        itemid = int(input("Enter Item (1 for Strength, 2 for Resilience, 3 for Healing): "))
        yn = str(input(f"Are you sure you want to delete {shop_item_data[itemid-1]['type']} from the shop? (y/n) "))
        if yn.lower() == 'y':
            shop_item_data[itemid]["stock"] = 0
            print(f"{shop_item_data[itemid-1]['type']} has been deleted from the shop!")

# MAIN PROGRAM
print(">>> SHOP")
print("Ah.. it's good to see you again. Welcome!")

option = str(input("OPTIONS: VIEW / ADD / EDIT / DELETE / EXIT "))
# assume the user's input is always valid
while option.lower() != 'exit':
    if option.lower() == 'view':
        view()
    elif option.lower() == 'add':
        add()
    elif option.lower() == 'edit':
        edit()
    elif option.lower() == 'delete':
        delete()
    option = str(input("OPTIONS: VIEW / ADD / EDIT / DELETE / EXIT "))
if option.lower() == 'exit': 
    print("Alrighty, safe travels! Hope to see you again~")
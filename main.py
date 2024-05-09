import src.load as load
import src.save as save

users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data = load.load_files()


print(monster_data)
choice = input("wanna save y/n (testing)")
if choice == "y":
    save.save(users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)

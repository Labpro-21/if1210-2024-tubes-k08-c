import os


def csv_saver(folder_path: str, data_array: list[dict[str, str]], file_name:str):
    save_file_path = os.path.join(folder_path, file_name)
    with open(save_file_path, 'w') as file:
        data_array_headers = list(data_array[0].keys())
        for header_index in range(len(data_array_headers)):
            file.write(data_array_headers[header_index])
            if header_index != len(data_array_headers)-1:
                file.write(";")
            else:
                file.write("\n")
        for row in data_array:
            curr_row_values = list(row.values())
            for value_index in range(len(curr_row_values)):
                file.write(curr_row_values[value_index])
                if value_index != len(curr_row_values) - 1:
                    file.write(";")
                else:
                    file.write("\n")


def save(user_data: list[dict[str, str]],
         monster_data: list[dict[str, str]],
         inv_item_data: list[dict[str, str]],
         inv_monster_data: list[dict[str, str]],
         shop_item_data: list[dict[str, str]],
         shop_monster_data: list[dict[str, str]]):
    parent_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),"data")
    target_folder = input("Enter save folder name : ")
    save_path = os.path.join(parent_path, target_folder)
    print("Saving, do not exit program")
    if os.path.isdir(save_path):
        pass
    else:
        os.makedirs(save_path)
        print("Creating folder at data/{}".format(target_folder))
    csv_saver(save_path, user_data, "user.csv")
    csv_saver(save_path, monster_data, "monster.csv")
    csv_saver(save_path, inv_item_data, "item_inventory.csv")
    csv_saver(save_path, inv_monster_data, "monster_inventory.csv")
    csv_saver(save_path, shop_item_data, "item_shop.csv")
    csv_saver(save_path, shop_monster_data, "monster_shop.csv")
    print("Save succesful at data/{}".format(target_folder))
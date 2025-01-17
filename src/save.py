import os


# csv writer function
def csv_saver(folder_path: str, data_array: list[dict], file_name: str):
    save_file_path = os.path.join(folder_path, file_name)
    # opens file
    with open(save_file_path, 'w') as file:
        # writes the headers first
        data_array_headers = list(data_array[0].keys())
        for header_index in range(len(data_array_headers)):
            file.write(data_array_headers[header_index])
            if header_index != len(data_array_headers)-1:
                file.write(";")
            else:
                file.write("\n")
        # writes the values per row
        for row in data_array:
            curr_row_values = list(row.values())
            for value_index in range(len(curr_row_values)):
                file.write(str(curr_row_values[value_index]))
                if value_index != len(curr_row_values) - 1:
                    file.write(";")
                else:
                    file.write("\n")


# save mechanism function
def save(user_data: list[dict],
         monster_data: list[dict],
         inv_item_data: list[dict],
         inv_monster_data: list[dict],
         shop_item_data: list[dict],
         shop_monster_data: list[dict]):
    # path designation
    parent_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
                               "data")
    target_folder = input("Enter save folder name : ")
    save_path = os.path.join(parent_path, target_folder)
    print("Saving, do not exit program")
    if os.path.isdir(save_path):
        pass
    # creates new folder if specified folder does not exist
    else:
        os.makedirs(save_path)
        print("Creating folder at data/{}".format(target_folder))
    # saves all the data
    csv_saver(save_path, user_data, "user.csv")
    csv_saver(save_path, monster_data, "monster.csv")
    csv_saver(save_path, inv_item_data, "item_inventory.csv")
    csv_saver(save_path, inv_monster_data, "monster_inventory.csv")
    csv_saver(save_path, shop_item_data, "item_shop.csv")
    csv_saver(save_path, shop_monster_data, "monster_shop.csv")
    print("Save succesful at data/{}".format(target_folder))

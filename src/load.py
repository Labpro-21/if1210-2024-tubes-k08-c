import argparse
import os


def csv_to_dict(file_name: str) -> list[dict]:
    # add a row
    rows = []
    with open(file_name, 'r') as file:
        lines = []
        line = ''
        while True:
            # reads the file one-by-one
            char = file.read(1)
            # breaks when it reaches the end
            if char == '':
                if line != "":
                    lines.append(line)
                break
            # add a line if line end is reached
            if char == '\n':
                lines.append(line)
                line = ''
            # add char to line
            else:
                line += char

        # get headers for dict
        headers = []
        header = ''
        index = 0
        for char in lines[0]:
            # adds a header if ";" is reached and prepares for a new one
            if char == ';':
                headers.append(header)
                header = ''
            # add chars to header
            else:
                header += char
                if index == len(lines[0]) - 1:
                    headers.append(header)
            index += 1
        # loop lines ignoring the first line
        for line in lines[1:]:
            fields = []
            field = ''
            index = 0
            # appends field when ";" is reached
            for char in line:
                if char == ';':
                    fields.append(field)
                    field = ''
                else:
                    field += char
                    if index == len(line) - 1:
                        fields.append(field)
                index += 1
            # append rows of dicts

            row_dict = {}
            for i in range(len(headers)):
                row_dict[headers[i]] = fields[i]
            rows.append(row_dict)
    return rows


def convert_realvalues_dict(arr_key_int: list[str], arr_dict: list[dict]) -> list[dict]:
    # arrKeyInt -> list of string key dari data Integer
    # arrDict -> List Of Dictionary
    arrdictcopy = arr_dict[:]
    for i in range(len(arr_dict)):
        for j in range(len(arr_key_int)):
            arrdictcopy[i][arr_key_int[j]] = int(arrdictcopy[i][arr_key_int[j]])
    return arrdictcopy


def load_files() -> (list[dict],
                     list[dict],
                     list[dict],
                     list[dict],
                     list[dict],
                     list[dict]):
    # gets current file parent
    parent_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data")
    # argparser setup
    load_parser = argparse.ArgumentParser(description="Save file loader")
    load_parser.add_argument("folder_path", help="Input the save file folder path", type=str)
    load_args = load_parser.parse_args()
    # target path
    target_path = os.path.join(parent_path, load_args.folder_path)
    # folder name not given
    if load_args.folder_path == "":
        print("No folder name was given, exiting program")
        exit()
    # folder found
    if os.path.isdir(target_path):
        print("Initializing......")
        # get files paths
        users_path = os.path.join(target_path, "user.csv")
        monster_data_path = os.path.join(target_path, "monster.csv")
        inv_item_path = os.path.join(target_path, "item_inventory.csv")
        inv_monster_path = os.path.join(target_path, "monster_inventory.csv")
        shop_item_path = os.path.join(target_path, "item_shop.csv")
        shop_monster_path = os.path.join(target_path, "monster_shop.csv")

        # load to each list of dictionaries
        users_data = convert_realvalues_dict(['id', 'oc'], csv_to_dict(users_path))
        monster_data = convert_realvalues_dict(['id', 'atk_power', 'def_power', 'hp'], csv_to_dict(monster_data_path))
        inv_item_data = convert_realvalues_dict(['user_id', 'quantity'], csv_to_dict(inv_item_path))
        inv_monster_data = convert_realvalues_dict(['user_id', 'monster_id', 'level'], csv_to_dict(inv_monster_path))
        shop_item_data = convert_realvalues_dict(['stock', 'price'], csv_to_dict(shop_item_path))
        shop_monster_data = convert_realvalues_dict(['monster_id', 'stock', 'price'], csv_to_dict(shop_monster_path))
        print()
        print("Program Loaded")
        print("Welcome to OWCA Agent")
        return users_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data
    # folder not found
    else:
        print("Folder \"{}\" was not found, exiting program".format(load_args.folder_path))
        exit()

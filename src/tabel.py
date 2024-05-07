# fungsi tabel() berfungsi untuk mebuat tabel yang sesuai dengan format tubes

dict_1 = [{'id': '1', 'type': 'Pikachow', 'atk_power': '125', 'def_power': '10', 'hp': '600'}, 
          {'id': '2', 'type': 'Bulbu', 'atk_power': '50', 'def_power': '50', 'hp': '1200'}, 
          {'id': '3', 'type': 'Zeze', 'atk_power': '300', 'def_power': '10', 'hp': '100'}, 
          {'id': '4', 'type': 'Zuko', 'atk_power': '100', 'def_power': '25', 'hp': '800'}, 
          {'id': '5', 'type': 'Chacha', 'atk_power': '80', 'def_power': '30', 'hp': '7006'}] # Sebagai Contoh

def tabel(df,row_1): # df merupakan list-nya dan row_1 merupakan list index-nya
    list_key = list(dict_1[0].keys())
    list_len = [[len(i)] for i in list_key]
    max_len = []
    for i in range(len(df)):
        for j in range(len(list_key)):
            list_len[j].append(len(df[i][list_key[j]]))

    for i in list_len:
        max_len.append(max(i))

    for i in range(len(list_key)):
        if i < len(list_key)-1:
            ending = '| '
        else:
            ending = '\n'
        print(f"{row_1[i]}{' '*(max_len[i] - len(list_key[i]))} ",end=ending) 

    for i in range(len(df)):
        for j in range(len(list_key)):
            if j < len(list_key)-1:
                ending2 = '| '
            else:
                ending2 = '\n'
            print(f"{df[i][list_key[j]]}{" "*(max_len[j] - list_len[j][i+1])} ",end=ending2)
    print("\n")

tabel(dict_1,['ID','Type','ATK Power','DEF Power','HP']) # Sebagai contoh
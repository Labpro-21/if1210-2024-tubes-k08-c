import load
import os

df_path = os.path.join("data/","init/","monster.csv")

def tabel_monster(df):
    list_len = [[2],[4],[9],[9],[2]]
    max_len = []
    for i in range(len(df)):
        list_len[0].append(len(df[i]["id"]))
        list_len[1].append(len(df[i]["type"]))
        list_len[2].append(len(df[i]["atk_power"]))
        list_len[3].append(len(df[i]["def_power"]))
        list_len[4].append(len(df[i]["hp"]))

    for i in list_len:
        max_len.append(max(i))

    print(f"ID{' '*(max_len[0] - 2)} | Type{' '*(max_len[1] - 4)} | ATK Power{' '*(max_len[2] - 9)} | DEF Power{' '*(max_len[3] - 9)} | HP{' '*(max_len[4] - 2)}" )
    for i in range(len(df)):
        print(f"{df[i]["id"]}{" "*(max_len[0] - list_len[0][i+1])} | {df[i]["type"]}{" "*(max_len[1] - list_len[1][i+1])} | {df[i]["atk_power"]}{" "*(max_len[2] - list_len[2][i+1])} | {df[i]["def_power"]}{" "*(max_len[3] - list_len[3][i+1])} | {df[i]["hp"]}{" "*(max_len[4] - list_len[4][i+1])}")
    print("\n")

def csv_append(df_path,id,type_name,atk_power,def_power,hp):
    csv_file = open(df_path,"a")
    csv_file.writelines(f"\n{id};{type_name};{atk_power};{def_power};{hp}")
    csv_file.close()

def validasi_int(angka):
    try:
        int(angka)
        return True
    except:
        return False

def ui_monster():
    min_def,max_def = 0,50
    while True:
        df = load.csv_to_dict(df_path)
        list_name = [df[i]['type'] for i in range(len(df))]
        print("""SELAMAT DATANG DI DATABASE PARA MONSTER !!!
1. Tampilkan semua Monster pada database
2. Tambah Monster baru
3. Keluar
""")
        pilihan = input("Pilih Aksi : ")
        if pilihan == "1":
            tabel_monster(df)
        elif pilihan == "2":
            id = str(int(df[len(df)-1]["id"])+1)
            while True:
                type_name = input("Masukkan Type / Nama : ")
                if type_name not in list_name:
                    break
                else:
                    print("Nama sudah terdaftar, coba lagi!\n")
            while True:
                atk_power = input("Masukkan ATK Power : ")
                if validasi_int(atk_power):
                    break
                else:
                    print("Masukkan input berupa Integer, coba lagi!\n")
            while True:
                def_power = input("Masukkan DEF Power : ")
                if validasi_int(def_power):
                    if min_def <= int(def_power) <= max_def:
                        break
                    else:
                        print(f"DEF Power harus bernilai {min_def}-{max_def}, coba lagi!\n")
                else:
                    print("Masukkan input berupa Integer, coba lagi!\n")
            while True:
                hp = input("Masukkan HP : ")
                if validasi_int(hp):
                    break
                else:
                    print("Masukkan input berupa Integer, coba lagi!\n")

            print(f"""
Monster baru berhasil dibuat!
Type : {type_name}
ATK Power : {atk_power}
DEF Power : {def_power}
HP : {hp}
""")
            while True:
                pilihan2 = input("Tambahkan Monster ke Database (Y/N): ")
                if pilihan2 == "Y" or pilihan2 == "y":
                    csv_append(df_path,id,type_name,atk_power,def_power,hp)
                    print("Monster berhasil ditambahkan!\n")
                    break
                elif pilihan2 == "N" or pilihan2 == "n":
                    print("Monster gagal ditambahkan!\n")
                    break
                else:
                    print("Masukkan tidak valid")
        elif pilihan == "3":
            break

        else:
            print("Masukkan tidak valid")
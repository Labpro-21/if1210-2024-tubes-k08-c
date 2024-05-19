import os
import time
import lcg
import ascii_art as art


def gacha(user_id: int,
          user_coin: int,
          user_data: list[dict],
          monster_data: list[dict],
          inv_monster_data: list[dict]) \
          -> (list[dict], list[dict]):
    terminal_width = os.get_terminal_size().columns
    print("$" * terminal_width)
    print("$" * ((terminal_width - 30) // 2)
          + "    Welcome to OWCA Gacha!    "
          + "$" * ((terminal_width - 30) // 2))
    print("$" * ((terminal_width - 30) // 2)
          + "    Pay 250 OC to PLAY!!!!    "
          + "$" * ((terminal_width - 30) // 2))
    print("$" * terminal_width)
    print()
    print("====ITEM LIST====")
    gacha_items = [{"id": 1, "item": "Fedora", "oc": 40},
                   {"id": 2, "item": "Watch", "oc": 60},
                   {"id": 3, "item": "Gold", "oc": 100},
                   {"id": 4, "item": "Dragon", "oc": 200},
                   {"id": 5, "item": "Bomb", "oc": -50}]
    for row in gacha_items:
        print(f"{row['id']}. {row['item']} : {row['oc']} OC")
    print("Get three of a kind and receive a monster!!!")
    print("There may even be a hidden reward >< !!!")
    while True:
        play_choice = input("Would you like to play (Y/N)? : ").upper()
        if play_choice == "Y":
            if user_coin < 250:
                print("Sorry you don't have enough OWCA Coins")
                print("Come back next time !!!")
                break
            else:
                user_coin -= 250
                print("GET READY TO GACHAAAAAAAA")
                for i in range(terminal_width):
                    print(".", end="", flush=True)
                    time.sleep(1 / terminal_width)
                print("YOU ROLLED !!!! : ")
                time.sleep(1)
                # super jackpot trigger
                special_roll = lcg.randint1(1, 50)
                # special event
                if special_roll == 50:
                    art.ryou_jackpot()
                    print("うわぁぁぁぁぁぁぁ、特別報酬が当たったんだね!!!")
                    print("「3000 OC」を受け取った!!")
                    total_gains = 3000
                    user_coin += 3000

                # normal gacha rewards
                else:
                    total_gains = 0
                    rolled_item = []
                    for slot_times in range(3):
                        slot_id = lcg.randint1(1, 5)
                        print("|", end="", flush=True)
                        for i in range(4):
                            print(" ", end="", flush=True)
                            time.sleep(0.25)
                        print(gacha_items[slot_id - 1]['item'], end="", flush=True)
                        rolled_item.append(gacha_items[slot_id - 1]['item'])
                        total_gains += gacha_items[slot_id - 1]['oc']
                    print()
                    # three of a kind
                    if (rolled_item[0] == rolled_item[1]) and \
                            rolled_item[1] == rolled_item[2]:
                        type_monster = lcg.randint1(0, len(monster_data) - 1)
                        level_monster = lcg.randint1(1, 3)
                        print(f"MONSTER JACKPOTTTT  YOU'VE WON A LEVEL {level_monster} "
                              f"{monster_data[type_monster]['type']}")
                        inv_monster_data.append({'user_id': user_id,
                                                 "monster_id": type_monster,
                                                 "level": level_monster})

                user_coin += total_gains
                if user_coin < 0:
                    user_coin = 0
                else:
                    pass
                if total_gains < 250:
                    print(f"Oops, you lost {250-total_gains} OC. Better luck next time")
                else:
                    print(f"Congrats, you gained {total_gains} OC. Come again !!!")
                print(f"Your current balance is {user_coin} OC")
                user_data[user_id-1]['oc'] = user_coin

        elif play_choice == "N":
            print("See you next time")
            break
        else:
            print("Enter a valid choice")
            print()
    return user_data, inv_monster_data

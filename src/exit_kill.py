import save


def exit_kill(user_data: list[dict],
              monster_data: list[dict],
              inv_item_data: list[dict],
              inv_monster_data: list[dict],
              shop_item_data: list[dict],
              shop_monster_data: list[dict]):
    while True:
        save_choice = input("Do you want to save before exiting? (Y/N):").upper()
        if save_choice == "Y":
            save.save(user_data, monster_data, inv_item_data, inv_monster_data, shop_item_data, shop_monster_data)
            print("See you next time agent !!!")
            break
        elif save_choice == "N":
            print("See you next time agent !!!")
            break
        else:
            print("Enter a valid choice")

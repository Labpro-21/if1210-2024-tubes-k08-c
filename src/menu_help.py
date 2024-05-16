def help_ui(status: str, username:str):
    if status == "agent":
        print(f"""=========== HELP ===========

Hello Agent {username}. Since you requested HELP, here are your available actions:

1. LOGOUT: Log out from your account
2. SHOP: Visit the Shop to purchase items or monsters
3. MONSTER: View your OWCA-Dex to see owned monsters
4. LAB: Upgrade the monsters you own
5. BATTLE: Engage in battle with enemies
6. ARENA: Fight hordes of monsters in the Arena
7. GACHA: Play and win lots of OWCA Coins !!! 
8. SAVE: Save current progress and data
9. EXIT: Exit the game
""")
    
    elif status == "admin":
        print("""=========== HELP ===========

Welcome back, Admin. Since you requested HELP, here are your available actions:

1. LOGOUT: Log out from your account
2. SHOP: Manage the SHOP stock for agents to buy from
3. MONSTER: Add or Remove monsters from the database
4. SAVE: Save current progress and data
5. EXIT: Exit the game
""")



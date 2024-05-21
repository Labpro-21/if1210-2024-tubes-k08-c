# fungsi untuk membuat textbox (hiasan)
def textbox(text):
    print("╔" + "═"*(len(text)+2) + "╗")
    print("║" + " " + text + " " + "║")
    print("╚" + "═"*(len(text)+2) + "╝")
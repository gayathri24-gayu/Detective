import time
import json

inventory = []
clues = 0
suspicions = 0

def show_intro():
    print("Welcome to the Extended Detective Mystery Adventure!")
    time.sleep(1)
    print("You are a detective in a noir-style city. Solve the mystery to win!\n")
    time.sleep(1)

def choose_location():
    print("You have four locations to investigate: the crime scene, the suspect's house, the old warehouse, and the victim's apartment.")
    choice = input("Where do you want to go first? Type 'crime scene', 'house', 'warehouse', or 'apartment': ").lower()
    while choice not in ['crime scene', 'house', 'warehouse', 'apartment']:
        choice = input("Invalid choice. Type 'crime scene', 'house', 'warehouse', or 'apartment': ").lower()
    return choice

def crime_scene():
    global clues, suspicions
    print("You arrived at the crime scene. You find a bloody knife and a torn piece of fabric.")
    time.sleep(1)
    choice = input("Do you want to 'take' the knife and fabric or 'leave' them? ").lower()
    while choice not in ['take', 'leave']:
        choice = input("Invalid choice. Type 'take' or 'leave': ").lower()
    if choice == 'take':
        inventory.append("Bloody Knife")
        inventory.append("Torn Fabric")
        clues += 1
        suspicions += 1
        print(f"Clues collected: {clues}")
        print(f"Inventory: {inventory}")
    else:
        print("You left the knife and fabric at the crime scene.")
    choose_next_location()

def house():
    global clues, suspicions
    print("You arrived at the suspect's house. You find a suspicious letter and a locked box.")
    time.sleep(1)
    choice = input("Do you want to 'read' the letter or 'ignore' it? ").lower()
    while choice not in ['read', 'ignore']:
        choice = input("Invalid choice. Type 'read' or 'ignore': ").lower()
    if choice == 'read':
        inventory.append("Suspicious Letter")
        clues += 1
        suspicions += 1
        print(f"Clues collected: {clues}")
        print(f"Inventory: {inventory}")
    else:
        print("You ignored the letter.")
    choice = input("Do you want to 'break' the locked box or 'leave' it? ").lower()
    while choice not in ['break', 'leave']:
        choice = input("Invalid choice. Type 'break' or 'leave': ").lower()
    if choice == 'break':
        inventory.append("Locked Box")
        suspicions += 1
        print(f"Suspicions increased: {suspicions}")
        print(f"Inventory: {inventory}")
    else:
        print("You left the locked box at the house.")
    choose_next_location()

def warehouse():
    global clues, suspicions
    print("You arrived at the old warehouse. You find a hidden stash of money and a mysterious key.")
    time.sleep(1)
    choice = input("Do you want to 'take' the money and key or 'leave' them? ").lower()
    while choice not in ['take', 'leave']:
        choice = input("Invalid choice. Type 'take' or 'leave': ").lower()
    if choice == 'take':
        inventory.append("Hidden Money")
        inventory.append("Mysterious Key")
        clues += 1
        suspicions += 1
        print(f"Clues collected: {clues}")
        print(f"Inventory: {inventory}")
    else:
        print("You left the money and key at the warehouse.")
    choose_next_location()

def apartment():
    global clues, suspicions
    print("You arrived at the victim's apartment. You find a diary and a photo.")
    time.sleep(1)
    choice = input("Do you want to 'read' the diary or 'ignore' it? ").lower()
    while choice not in ['read', 'ignore']:
        choice = input("Invalid choice. Type 'read' or 'ignore': ").lower()
    if choice == 'read':
        inventory.append("Diary")
        clues += 1
        print(f"Clues collected: {clues}")
        print(f"Inventory: {inventory}")
    else:
        print("You ignored the diary.")
    choice = input("Do you want to 'take' the photo or 'leave' it? ").lower()
    while choice not in ['take', 'leave']:
        choice = input("Invalid choice. Type 'take' or 'leave': ").lower()
    if choice == 'take':
        inventory.append("Photo")
        suspicions += 1
        print(f"Suspicions increased: {suspicions}")
        print(f"Inventory: {inventory}")
    else:
        print("You left the photo at the apartment.")
    solve_mystery()

def solve_mystery():
    if clues >= 3 and suspicions >= 3:
        print("You have collected enough clues and managed your suspicions well. Congratulations, you solved the mystery!")
    else:
        print("You haven't collected enough clues or managed your suspicions well. Keep investigating.")
        choose_next_location()

def choose_next_location():
    choice = choose_location()
    if choice == 'crime scene':
        crime_scene()
    elif choice == 'house':
        house()
    elif choice == 'warehouse':
        warehouse()
    else:
        apartment()

def save_game():
    game_data = {
        'inventory': inventory,
        'clues': clues,
        'suspicions': suspicions
    }
    with open('savegame.json', 'w') as savefile:
        json.dump(game_data, savefile)
    print("Game saved successfully!")

def load_game():
    global inventory, clues, suspicions
    try:
        with open('savegame.json', 'r') as savefile:
            game_data = json.load(savefile)
            inventory = game_data['inventory']
            clues = game_data['clues']
            suspicions = game_data['suspicions']
            print("Game loaded successfully!")
    except FileNotFoundError:
        print("No saved game found.")

def main():
    while True:
        print("\nMain Menu:")
        print("1. Start New Game")
        print("2. Load Game")
        print("3. Exit")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            show_intro()
            path = choose_location()
            if path == 'crime scene':
                crime_scene()
            elif path == 'house':
                house()
            elif path == 'warehouse':
                warehouse()
            else:
                apartment()
        elif choice == '2':
            load_game()
        elif choice == '3':
            save_game()
            print("Exiting the game. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()

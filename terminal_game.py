

import time

print("🏰 Welcome to the Enchanted Castle Adventure! 🏰")
print("Your goal is to escape alive. Beware of the dangers...\n")
time.sleep(1)

# Game variables
hp = 100
has_key = False
game_over = False

# Main loop: The game continues while you have health and haven't finished
while not game_over and hp > 0:
    print("-" * 40)
    print(f"❤️  Current HP: {hp} | 🗝️  Key: {'Yes' if has_key else 'No'}")
    print("You are in the Great Hall. You have three paths:")
    print("1. Go left (Kitchen)")
    print("2. Go right (Library)")
    print("3. Go forward (Main Door)")
    
    # Main decision making
    choice = input("\nWhat do you choose to do? (Choose 1, 2, or 3): ")
    
    if choice == "1":
        print("\nYou enter the kitchen. It's very dark and you hear a strange noise.")
        print("1. Open the mysterious cupboard.")
        print("2. Run back to the Great Hall.")
        
        kitchen_choice = input("What do you do? (1 or 2): ")
        
        if kitchen_choice == "1":
            print("\nOh no! A goblin jumped out of the cupboard and attacked you.")
            hp -= 30
            print("You lose 30 health points. You manage to escape back to the hall.")
        elif kitchen_choice == "2":
            print("\nYou return safely to the Great Hall.")
        else:
            print("\nYou get nervous and trip, stumbling back to the Great Hall.")
            
    elif choice == "2":
        print("\nYou enter the dusty library. You see a glowing chest on a table.")
        print("1. Open the chest.")
        print("2. Ignore the chest and return to the Great Hall.")
        
        library_choice = input("What do you do? (1 or 2): ")
        
        if library_choice == "1":
            if not has_key:
                print("\nYou found the Golden Key! This might open the main door.")
                has_key = True
            else:
                print("\nThe chest is empty. You already took the key.")
        else:
            print("\nYou return to the Great Hall without touching anything.")
            
    elif choice == "3":
        print("\nYou approach the massive Main Door. It has a heavy lock.")
        
        if has_key:
            print("You use the Golden Key and the door creaks open!")
            print("\n🎉 Congratulations! You escaped the Enchanted Castle and won the game. 🎉")
            game_over = True
        else:
            print("The door is locked. You need to find a key to open it.")
            print("You return to the Great Hall to keep searching.")
            
    else:
        print("\n❌ Please choose a valid option (1, 2, or 3).")

if hp <= 0:
    print("\n💀 You have run out of health points. Game Over!")
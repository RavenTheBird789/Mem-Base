# MemoryBase

import os
import time
import hashlib

def bold(text: str) -> str:
    return f"\033[1m{text}\033[0m"

def red(text: str) -> str:
    return f"\033[91m{text}\033[0m"

def pink(text: str) -> str:
    return f"\033[48;2;255;105;180m{text}\033[0m"

def green(text: str) -> str:
    return f"\033[92m{text}\033[0m"

def yellow(text: str) -> str:
    return f"\033[93m{text}\033[0m"

if os.path.exists("username.txt"):
    user_authentication = ""
    with open("username.txt", "r", encoding="utf-8") as u:
        user_authentication = u.read().strip()

    # Initialization of memories from memories.txt
    def init_mems():
        if os.path.exists("memories.txt"):
            with open("memories.txt", "r") as ms:
                return [line.strip() for line in ms if line.strip()]
        return []

    def remember(mem_list):
        with open("memories.txt", "w") as mem:
            mem.write("\n".join(mem_list))

    username = input("What is your name?: ").strip()
    hashed_user_authentication = hashlib.sha3_512(username.encode()).hexdigest()

    if hashed_user_authentication == user_authentication:
        time.sleep(0.5)
        print(green("Access Granted"))
        time.sleep(0.5)
        print((f"Welcome, {username} ") + yellow(":)"))
        time.sleep(0.5)
        os.system("cls" if os.name == 'nt' else 'clear')

        def show_mems():
            mem_list = init_mems()
            i = 0
            for mem in mem_list:
                i += 1
                print(f"{i}. {mem}")

        def add_mem():
            mem_list = init_mems()
            prompt = input("What would you like to remind yourself to do later?: ")
            if prompt:
                mem_list.append(prompt)
                remember(mem_list)
                print(green("Your memories have been successfully updated!"))
            else:
                os.system("cls" if os.name == 'nt' else 'clear')
                print(yellow("Input field empty.\nReturning to the main menu."))
                time.sleep(3)
                main()

        def rem_mem():
            mem_list = init_mems()
            try:
                show_mems()
                prompt = int(input("Which memory would you like to forget? (Enter the number): "))
                indx_val = prompt - 1
                del mem_list[indx_val]
                remember(mem_list)
            except ValueError:
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input"))
                time.sleep(1)
                os.system("cls" if os.name == 'nt' else 'clear')
                main();                

        def change_mem():
            mem_list = init_mems()
            try:
                show_mems()
                prompt = int(input("Which memory would you like to alter? (Enter the number): "))
                indx_val = prompt - 1
                mem_list[indx_val] = input("Enter whatever you'd like to remember instead: ").strip()
                remember(mem_list)
            except ValueError:
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input"))
                time.sleep(1)
                os.system("cls" if os.name == 'nt' else 'clear')
                main();                  

        def nuke_all():
            try:
                os.remove("memories.txt")
                os.remove("username.txt") 
                print(green("All your data has successfully been forgotten."))
            except FileNotFoundError:
                print("No memories found to forget!")
                time.sleep(2)
                print("Forgetting name...")
                os.remove("username.txt")
                time.sleep(2)
                print(green("All your data has successfully been forgotten."))

        def main_menu():
            user_query = input("Would you like to return to the main menu? (yes/no): ").lower().strip()
            if user_query == "yes":
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Returning to the main menu"))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Returning to the main menu" + ("." * 1)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Returning to the main menu" + ("." * 2)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Returning to the main menu" + ("." * 3)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                main();
            elif user_query == "no":
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Exiting"))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Exiting" + ("." * 1)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Exiting" + ("." * 2)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(green("Exiting" + ("." * 3)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                os._exit(0);
            else:
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input. Returning to the main menu"))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input. Returning to the main menu" + ("." * 1)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input. Returning to the main menu" + ("." * 2)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input. Returning to the main menu" + ("." * 3)))
                time.sleep(0.5)
                os.system("cls" if os.name == 'nt' else 'clear')
                main();
 
        def trademark(main_func):
            def wrapper():
                print("  ________________  ")
                print(" /                \\")
                print("|------------------|")
                print(("|---| ") + bold(pink("Mem-Base")) + (" |---|"))
                print("|------------------|")
                print(("|") + bold(red("By RavenTheBird789")) + ("|"))
                print("|------------------|")
                print("|---|  v1.1.0  |---|")
                print("|__________________|\n")
                main_func()
            return wrapper

        @trademark
        def main():
            print("=================================")
            print("Option 1: Show me all my memories")
            print("Option 2: Add a new memory")
            print("Option 3: Forget a memory")
            print("Option 4: Alter a memory")
            print("Option 5: Forget all memories")
            print("Option 6: Exit")
            print("=================================")
            try:
                user_choice = int(input("Please choose an option: "))
                if user_choice == 1:
                    os.system("cls" if os.name == 'nt' else 'clear')
                    print(f"{username}, Don't Forget To Do The Following:")
                    print("-" * 40)
                    show_mems()
                    time.sleep(2)
                    main_menu();
                elif user_choice == 2:
                    os.system("cls" if os.name == 'nt' else 'clear')
                    add_mem()
                    time.sleep(2)
                    main_menu();
                elif user_choice == 3:
                    os.system("cls" if os.name == 'nt' else 'clear')
                    rem_mem()
                    time.sleep(2)
                    main_menu();
                elif user_choice == 4:
                    os.system("cls" if os.name == 'nt' else 'clear')
                    change_mem()
                    time.sleep(2)
                    main_menu()
                elif user_choice == 5:
                    os.system("cls" if os.name == 'nt' else 'clear')
                    user_prompt = input("Are you sure you want to forget everything? (yes/no): ").strip().lower()
                    if user_prompt:
                        if user_prompt == "yes":
                            nuke_all()
                            time.sleep(2)
                            main_menu();
                        elif user_prompt == "no":
                            os.system("cls" if os.name == 'nt' else 'clear')
                            main();
                        else:
                            os.system("cls" if os.name == 'nt' else 'clear')
                            print(red("Invalid Input"))
                            time.sleep(2)
                            main();
                    else:
                        os.system("cls" if os.name == 'nt' else 'clear')
                        print(yellow("Input field empty.\nReturning to the main menu."))
                        time.sleep(3)
                        main()
                elif user_choice == 6:
                    os.system("cls" if os.name == 'nt' else 'clear')
                    print(green("Exiting"))
                    time.sleep(0.5)
                    os.system("cls" if os.name == 'nt' else 'clear')
                    print(green("Exiting" + ("." * 1)))
                    time.sleep(0.5)
                    os.system("cls" if os.name == 'nt' else 'clear')
                    print(green("Exiting" + ("." * 2)))
                    time.sleep(0.5)
                    os.system("cls" if os.name == 'nt' else 'clear')
                    print(green("Exiting" + ("." * 3)))
                    time.sleep(0.5)
                    os.system("cls" if os.name == 'nt' else 'clear')
                    os._exit(0);              
                else:
                    time.sleep(1)
                    os.system("cls" if os.name == 'nt' else 'clear')
                    print(red("Invalid Input"))
                    time.sleep(2)
                    main();
            except ValueError:
                time.sleep(1)
                os.system("cls" if os.name == 'nt' else 'clear')
                print(red("Invalid Input"))
                time.sleep(1)
                os.system("cls" if os.name == 'nt' else 'clear')
                main();
        main()
    else:
        print(red("Access Denied"))
        os._exit(0);

else:
    user_name = input("Hello! Please enter your name: ").strip()
    if user_name:
        hashed_user_name = hashlib.sha3_512(user_name.encode()).hexdigest()
        with open("username.txt", "w") as un:
            un.write("".join(hashed_user_name))
    os.system("cls" if os.name == 'nt' else 'clear')
    print("Please, run the script again.")
    os._exit(0);

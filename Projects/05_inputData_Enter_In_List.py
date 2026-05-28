my_List = []

while True:
    print("===========================================")
    print("             By Sagar Nautiyal             ")
    print("===========================================")
    print("[+] 1. Enter Data")
    print("[-] 2. Remove Data")
    print("[] 3. Show List")
    print("[=>] 4. Exit")

    # try-except block taaki galat input par code crash na ho
    try:
        choice = int(input("Enter the number between [1-4]: "))
    except ValueError:
        print("\n[!] Invalid input! Bhai, sirf numbers (1-4) hi allow hain.\n")
        continue

    # 1. Exit Logic
    if choice == 4:
        print("\nExiting... Bye Bhai! 👋")
        break

    # 2. Add Data Logic
    elif choice == 1:
        num = input("Enter the element you want to store in List: ")
        my_List.append(num)
        print(f"\n[+] Added: {num}")
        print("[+] Element added to the list successfully!\n")
    
    # 3. Remove Data Logic
    elif choice == 2:
        if len(my_List) == 0:
            print("\n[-] List pehle se khali hai bro!\n")
        else:
            num = input("Enter the element you want to remove from the list: ")
            if num in my_List:
                my_List.remove(num)
                print("\n[-] Number removed successfully from the list!\n")
            else:
                print("\n[-] Number not found in the list!\n")
    
    # 4. Show List Logic
    elif choice == 3:
        print("\n--- Teri Current List ---")
        if len(my_List) == 0:
            print("[ Khali Hai ]")
        else:
            print(my_List)
        print("-------------------------\n")

    # 5. Invalid Number Handling
    else:
        print("\n[!] Invalid Option! Please choose between 1 and 4.\n")
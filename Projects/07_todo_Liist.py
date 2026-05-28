todo_list = []  # Isme data aise save hoga: [["Gym", "H"], ["Code", "M"]]

while True:
    print("===========================================")
    print("         Sagar's Priority To-Do            ")
    print("===========================================")
    print("[+] 1. Add Task with Priority")
    print("[]  2. Show Tasks (By Priority)")
    print("[=>] 3. Exit")
    
    try:
        choice = int(input("\nEnter choice [1-3]: "))
    except ValueError:
        print("\n[!] Invalid input! Bhai, sirf numbers (1-3) hi allow hain.\n")
        continue

    # 1. ADD TASK LOGIC
    if choice == 1:
        task = input("Kaam ka naam likho (e.g., Study Python): ")
        priority = input("Priority set karo (H = High, M = Medium, L = Low): ").upper() # .upper() se agar user 'h' likhega toh wo 'H' ban jayega

        # Validation: Agar user ne H, M, L ke alawa kuch aur likha
        if priority not in ['H', 'M', 'L']:
            print("\n[!] Galat priority! Sirf H, M, ya L hi daalein.\n")
            continue

        # Ek choti list banakar main list mein daal rahe hain
        todo_list.append([task, priority])
        print(f"\n[✓] '{task}' successfully add ho gaya!\n")

    # 2. SHOW TASK LOGIC (Asli Khel)
    elif choice == 2:
        if not todo_list:
            print("\n[-] List khali hai bro! Pehle kuch kaam add karo.\n")
            continue

        print("\n==============================")
        print("          YOUR TASKS          ")
        print("==============================")

        # --- STEP A: Pehle sirf HIGH priority wale tasks print karo ---
        print("\n🔴 HIGH PRIORITY:")
        high_count = 0
        for item in todo_list:
            if item[1] == 'H':  # index 1 par priority hai
                print(f"  - {item[0]}")  # index 0 par task ka naam hai
                high_count += 1
        if high_count == 0:
            print("  (Koi kaam nahi hai)")

        # --- STEP B: Phir sirf MEDIUM priority wale tasks print karo ---
        print("\n🟡 MEDIUM PRIORITY:")
        med_count = 0
        for item in todo_list:
            if item[1] == 'M':
                print(f"  - {item[0]}")
                med_count += 1
        if med_count == 0:
            print("  (Koi kaam nahi hai)")

        # --- STEP C: End mein LOW priority wale tasks print karo ---
        print("\n🟢 LOW PRIORITY:")
        low_count = 0
        for item in todo_list:
            if item[1] == 'L':
                print(f"  - {item[0]}")
                low_count += 1
        if low_count == 0:
            print("  (Koi kaam nahi hai)")
            
        print("\n==============================\n")

    # 3. EXIT LOGIC
    elif choice == 3:
        print("\nChalo bye bhai! Apne saare kaam time pe khatam kar lena. 👍\n")
        break

    else:
        print("\n[!] Invalid Option! Please choose between 1 and 3.\n")
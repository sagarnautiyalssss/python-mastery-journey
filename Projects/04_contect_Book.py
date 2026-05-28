import pandas as pd
contact_book = {}  # It's empty dict

while True:
    print("===========================================")
    print("        Sagar's Contact Directory          ")
    print("===========================================")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Show All")
    print("4. Exit")
    
    try:
        choice = int(input("Enter the number between [1-4]: "))
    except ValueError:
        print("\n[!] Invalid input! Bhai, sirf numbers (1-4) hi allow hain.\n")
        continue

    if choice == 1 :
        name = input("Enter your Name : ")
        mobile_No = int(input("Enter your number : "))

        # Save name and mobile number 
        contact_book[name] = mobile_No
        print("Successfully saved !")

    elif choice == 2 :
        name = input("Enter the name you want to search : ")
        if name in contact_book :
            # Yahan humne contact_book[name] ka use karke number print karwaya hai
            print(f"\n[✓] Name found! {name}'s Mobile Number: {contact_book[name]}\n")
        else :
            print("\n[!] Name not found !\n")

    elif choice == 3 :
        if not contact_book:
            print("\n[!] Directory khali hai bhai! Pehle contact add karo.\n")
        else:
            # contact_book.items() se Name aur Mobile alag alag ho jayenge
            df = pd.DataFrame(contact_book.items(), columns=['Name', 'Mobile Number'])
            print("\n", df, "\n")

    elif choice == 4 :
        print("\nDhanyawad! Bye bye, phir milenge.\n")
        break  # Loop se bahar nikalne ke liye taki program exit ho jaye

    else :
        print("\n[!] Invalid number ! Enter between [1-4]\n")
# Pehle hum saare functions define kar lete hain
def Add(n1, n2):
    return n1 + n2

def Sub(n1, n2):
    return n1 - n2 

def Multi(n1, n2):
    return n1 * n2

def Div(n1, n2):
    if n2 == 0:
        return "Error! Zero se divide nahi kar sakte."
    return n1 / n2

# Ab shuru hota hai main logic while loop ke saath
while True:
    print("\n--- SIMPLE CALCULATOR ---")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    
    choice = input("Apna option chune (1-5): ")
    
    # Agar user exit (5) chunka hai, toh seedhe bahar nikal jao, numbers maangne ki zaroorat nahi
    if choice == "5":
        print("Calculator band ho raha hai. Bye!")
        break
        
    # Agar choice 1 se 4 ke beech hai, tabhi numbers input maango
    if choice in ["1", "2", "3", "4"]:
        n1 = int(input("Enter the first number: "))
        n2 = int(input("Enter the second number: "))
        
        match choice:
            case "1":
                print(f"Result: {Add(n1, n2)}")
            case "2":
                print(f"Result: {Sub(n1, n2)}")
            case "3":
                print(f"Result: {Multi(n1, n2)}")
            case "4":
                print(f"Result: {Div(n1, n2)}")
    else:
        # Agar user 1-5 ke alawa kuch aur daalta hai
        print("[-] Invalid Options please check the options.")
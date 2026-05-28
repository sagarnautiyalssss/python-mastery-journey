import random

# Computer ne ek number soch liya
computer_number = random.randint(1, 50)

# Attempts count karne ke liye ek variable bana lete hain
attempts = 0

print("=== Welcome to Number Guessing Game ===")
print("Maine 1 se 50 ke beech ek number socha hai. Guess karo!")

while True:
    # 1. Input hamesha loop ke andar aayega taaki har baar naya chance mile
    user_Number = int(input("\nEnter your number: "))
    attempts += 1  # Har baar jab user guess karega, attempt badh jayega

    # 2. Agar guess ekdum sahi hai
    if user_Number == computer_number:
        print(f"🎉 Congratulations bhai! Tune {attempts} attempts mein sahi guess kiya!")
        break  # Game khatam, loop se bahar!

    # 3. Agar guess chota hai
    elif user_Number < computer_number:
        print("📉 Too Low! Thoda bada number try kar.")

    # 4. Agar guess bada hai
    else:
        print("📈 Too High! Thoda chota number try kar.")
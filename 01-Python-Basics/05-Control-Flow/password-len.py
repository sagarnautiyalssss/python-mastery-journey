# --- Scenario 1: Password Length Validator ---
print("\n[+] Running Scenario 1: Password Validator")
password = "Admin_Password_123"

# Pehle check karenge length, phir content
if len(password) >= 8:
    print("[+] Length Check: Passed (8+ characters)")
    if "_" in password:
        print("[+] Complexity Check: Passed (Contains underscore)")
        print("[*] Result: Strong Password!")
    else:
        print("[-] Complexity Check: Failed (Missing underscore)")
        print("[!] Result: Medium Password.")
else:
    print("[-] Length Check: Failed! Password is too short.")
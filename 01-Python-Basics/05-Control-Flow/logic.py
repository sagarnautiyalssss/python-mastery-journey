# Variable Diclare 

status_code = 403

if status_code == 200 :
    print("[+] Status code is Success Accessible dashboard !")
elif status_code == 403:
    print("[!] Warning: Forbidden Area! Need to bypass WAF.")
elif status_code == 404:
    print("[-] Error: Page Not Found.")
else:
    print("[?] Unknown Status Code.")
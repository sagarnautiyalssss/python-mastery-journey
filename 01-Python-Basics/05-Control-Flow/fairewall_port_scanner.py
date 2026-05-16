# --- Scenario 2: Firewall Port Alerter ---
print("\n[+] Running Scenario 2: Port Alerter")
open_port = 443  # SSH Port
is_internal_ip = False  # External access attempt

# Multiple conditions with 'and' / 'or'
if open_port == 80 or open_port == 443:
    print(f"[*] Port {open_port} is Open: Standard Web Traffic allowed.")
elif open_port == 22 and is_internal_ip == False:
    print(f"[🚨] CRITICAL ALERT: SSH Port 22 is exposed to the Public Internet!")
elif open_port == 3389 and is_internal_ip == False:
    print(f"[🚨] CRITICAL ALERT: RDP Port 3389 is exposed publicly!")
else:
    print(f"[*] Port {open_port} open: Requires manual investigation.")
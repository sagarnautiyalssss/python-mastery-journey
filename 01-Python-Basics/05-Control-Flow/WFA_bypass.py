# --- Scenario 3: WAF Block Simulator ---
print("\n[+] Running Scenario 3: WAF Status")
request_count = 150
user_agent = "BurpSuite"

if request_count > 100 or user_agent == "BurpSuite":
    print("[!] WAF Triggered: Suspicious activity detected!")
    print("[X] Action: IP temporarily blacklisted (403 Forbidden).")
else:
    print("[+] WAF Status: Clear. Traffic looks normal.")
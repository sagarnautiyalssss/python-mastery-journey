# --- 1. Simple Function (No Arguments) ---
def greeting():
    print("================================================")
    print("              It's NAUTIYAL G                   ")
    print("================================================")

# --- 2. Combined Vulnerability Checker Function ---
# Ek hi function sabhi services handle karega using if-elif-else
def check_vulnerability(service_name, service_version):
    
    # Apache Logic
    if service_name == "Apache" and service_version <= "2.4.41":
        return "Vulnerable to RCE!"
        
    # SSH Logic (Dono parameters ko standard string rakhte hain error se bachne ke liye)
    elif service_name == "SSH" and service_version == "7.2":
        return "Vulnerable to User Enumeration!"
        
    # Fallback/Safe Output
    else:
        return "Service appears to be SECURE or Unknown."

# ==================== FUNCTIONS CALLING ====================

greeting() 

# Apache Test
print("[*] Checking Apache Version...")
apache_result = check_vulnerability("Apache", "2.4.4.1")
print(f"Result: {apache_result}\n")

# SSH Test (Version 7.2 bheja, port 22 nahi)
print("[*] Checking SSH Version...")
ssh_result = check_vulnerability("SSH", "7.2")
print(f"Result: {ssh_result}\n")

# Safe Service Test
print("[*] Checking Nginx Version...")
nginx_result = check_vulnerability("Nginx", "1.25.0")
print(f"Result: {nginx_result}\n")
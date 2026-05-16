"""
PROJECT     : Intermediate Functions Mastery
AUTHOR      : @nautiyal_g
CATEGORY    : Phase 2 - Intermediate Level
DESCRIPTION : A single consolidated script mastering basic functions, return structures,
               Default arguments, *args, and **kwargs with security automation use cases.
USAGE       : python3 functions_master.py
"""

# ==============================================================================
# 🟢 PART 1: THE CORE BASICS OF FUNCTIONS
# ==============================================================================

# A. Simple Function (No Arguments)
def greeting():
    print("================================================")
    print("              It's NAUTIYAL G                   ")
    print("================================================")

# B. Function with Arguments (Inputs)
def target_scan(url):
    print(f"[*] Starting intense enumeration on: {url}")

# C. Function with Return Value (Outputs) & Logical Bug Fix (Using 'or')
def check_port_status(port):
    if port == 80 or port == 443:  # Corrected from 'and' to 'or'
        return "Allowed web traffic !"
    elif port == 22:
        return "Filtered (SSH - Restricted)"
    else:
        return "Closed !"


# ==============================================================================
# 🟡 PART 2: DEEP DIVE ADVANCED CONCEPTS & PRACTICAL TASKS
# ==============================================================================

# Task 1: Scanner with Default Port (Default Arguments)
def launch_scan(target_ip, scan_type="SYN"):
    print(f"[*] Scanning IP: {target_ip} with Scan Type: {scan_type}")

# Task 2: Mass Target Collector (*args)
def add_mass_targets(*targets):
    print(f"[~] DataType received: {type(targets)}") # Packed into a Tuple
    for target in targets:
        print(f"[+] Target Registered: {target}")  # Fixed singular loop variable

# Task 3: Ultimate Vulnerability Report Builder (**kwargs)
def build_report(**vuln_details):
    print(f"[~] DataType received: {type(vuln_details)}") # Packed into a Dictionary
    for key, value in vuln_details.items():
        print(f"{key.upper()} -> {value}")


# ==============================================================================
# 🚀 EXECUTION & TESTING LAB
# ==============================================================================
if __name__ == "__main__":

    print("\n--- 🟢 RUNNING PART 1: BASICS ---")
    greeting() 
    target_scan("Google.com")
    
    # Catching and printing return values
    port_result = check_port_status(443) 
    print(f"[->] Port 443 Status: {port_result}")
    
    port_result_2 = check_port_status(22)
    print(f"[->] Port 22 Status: {port_result_2}")


    print("\n--- 🟡 RUNNING PART 2: TASK 1 (Default Args) ---")
    launch_scan("10.0.0.1")        # Automatic 'SYN' aayega
    launch_scan("10.0.0.2", "UDP")  # 'UDP' override ho jayega


    print("\n--- 🟡 RUNNING PART 2: TASK 2 (*args) ---")
    add_mass_targets("phonics.edu", "api.phonics.edu", "admin.phonics.edu")


    print("\n--- 🟡 RUNNING PART 2: TASK 3 (**kwargs) ---")
    build_report(target="phonics.edu", cve="CVE-2024-XXXX", severity="CRITICAL")
    
    print("\n=================== ALL TESTS PASSED ===================")
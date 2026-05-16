# Functions creating using by def keyword 
# --- 1. Simple Function (No Arguments) ---
def greeting():
    print("================================================")
    print("              It's NAUTIYAL G                   ")
    print("================================================")

# --- 2. Function with Arguments (Inputs) ---
def target_scan(url):
    print(f"[*] Starting intense enumeration on: {url}")

# --- 3. Function with Return Value (Output) ---    
def check_port_status(port):
    if port == 80 or port == 443:  # Fixed 'and' to 'or'
        return "Allowed web traffic !"
    elif port == 22:
        return "Filtered (SSH - Restricted)"
    else:
        return "Closed !"
    
# ==================== CALLING THE FUNCTIONS ====================

greeting() # First function calling 

target_scan("Google.com") # Second function calling with argument

# Third function calling with print to catch the return value
port_result = check_port_status(443) 
print(f"[->] Port 443 Status: {port_result}")

port_result_2 = check_port_status(22)
print(f"[->] Port 22 Status: {port_result_2}")
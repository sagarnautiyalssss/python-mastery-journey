# Default Argument Example

def scan_port(ip, port = 80) :
    print(f"[*] Scanning IP: {ip} on Port: {port}")

# Call 1: Dono arguments diye
scan_port("192.168.1.1", 443)  # Output: Scanning IP: 192.168.1.1 on Port: 443

# Call 2: Port nahi diya, toh automatic 80 utha lega
scan_port("10.0.0.5") 

# Variable-Length Arguments (*args)
# *args Example (Accepts any number of arguments)

def target_list(*subdomains): # we can gives multipales arguments
    print(type(subdomains)) # Yeh background mein ek Tuple ban jata hai
    for sub in subdomains:
        print(f"[+] Found Subdomain: {sub}")

# Tum chahe 2 subdomains bhejo ya 4, function sab handle karega
target_list("api.target.com", "admin.target.com")
target_list("dev.com", "test.com", "staging.com", "prod.com")

# 3. Keyword Arguments (kwargs)

# **kwargs Example
def save_hunter_profile(**details):
    print(type(details)) # Yeh background mein ek Dictionary ban jata hai
    for key, value in details.items():
        print(f"{key.upper()}: {value}")

# Profiling dynamic data
save_hunter_profile(name="Sagar", handle="@nautiyal_g", rank=15)
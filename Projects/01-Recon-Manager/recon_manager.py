"""
PROJECT NAME : Target Recon Profile Manager
AUTHOR       : @nautiyal_g
PURPOSE      : This script automates the organization of reconnaissance data for penetration testing.
               It consolidates target infrastructure metadata, eliminates duplicate IP addresses, 
               and structures active subdomains.

CONCEPTS USED:
  - Variables & Data Types (Tracking status and metadata)
  - Tuples      (Storing static infrastructure like Core DNS nameservers)
  - Lists       (Managing dynamic subdomain discovery with sorting methods)
  - Sets        (Automatic deduplication of discovered target IP addresses)
  - Dictionaries(Creating a master nested data structure for the target profile)

USAGE        : python3 recon_manager.py
"""

# ==================== CODE STARTS HERE ====================

# 1. Variables and Data Types (Target General Info)
target_name = "Phonics University"
total_subdomains_found = 145      
success_rate = 94.5               
is_active_bounty = True           

# 2. Tuples (Fixed Infrastructure Data - Cannot be changed)
PRIMARY_NAMESERVERS = ("ns1.phonics.edu", "ns2.phonics.edu")

# 3. Lists (Discovered Subdomains - Mutable)
subdomains = ["api.phonics.edu", "admin.phonics.edu", "blog.phonics.edu"]
subdomains.append("vpn.phonics.edu") 
subdomains.sort()                    

# 4. Sets (The Duplicate Killer - Unique IP Addresses)
discovered_ips = {"192.168.1.1", "10.0.0.5", "192.168.1.1", "172.16.0.2"} 

# 5. Dictionaries (The Ultimate Recon Profile - Nested Structure)
recon_profile = {
    "target": target_name,
    "bounty_program": is_active_bounty,
    "infrastructure": {
        "dns": PRIMARY_NAMESERVERS,
        "active_subdomains": subdomains,
        "unique_ips": discovered_ips
    }
}

# --- OUTPUT PRINTS ---
print("=================== RECON REPORT ===================")
print(f"Target Name: {recon_profile['target']}")
print(f"Active Bounty: {recon_profile['bounty_program']}")
print(f"DNS Servers: {recon_profile['infrastructure']['dns']}")
print(f"Total Unique IPs Found: {len(recon_profile['infrastructure']['unique_ips'])}")
print(f"Subdomains List: {recon_profile['infrastructure']['active_subdomains']}")
print("====================================================")
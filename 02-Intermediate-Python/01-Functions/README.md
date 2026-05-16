# 📦 Functions & Modular Architecture (Intermediate Level)

Functions are reusable blocks of code designed to perform specific tasks. Instead of writing the same logic repeatedly, we wrap it in a function using the `def` keyword. In cybersecurity scripting (like mass automation, port scanning, or vulnerability checking), functions are critical for scalability.

---

## 🟢 Part 1: Core Basics of Functions

Every function requires a **definition** (how it works) and a **call** (triggering it to execute).

### 1. Simple Function (No Arguments)
Used for static tasks like displaying a tool banner or greeting the user.
```python
def greeting():
    print("================================================")
    print("              It's NAUTIYAL G                   ")
    print("================================================")

greeting() # Execution call


# 2. Function with Arguments (Inputs)
Arguments allow passing dynamic data (like target domains or IPs) into the function.

def target_scan(url):
    print(f"[*] Starting intense enumeration on: {url}")

target_scan("Google.com")

### 3. Function with Return Value (Outputs) & Logic Correction
The return keyword sends data back to the script.

def check_port_status(port):
    if port == 80 or port == 443:  # Fixed: Changed 'and' to 'or'
        return "Allowed web traffic !"
    elif port == 22:
        return "Filtered (SSH - Restricted)"
    else:
        return "Closed !"

# Catching the output inside a print function
print(check_port_status(443))


🟡 Part 2: Deep Dive Advanced Concepts

1. Default Arguments (Fallback Parameters)

def launch_scan(target_ip, scan_type="SYN"):
    print(f"[*] Scanning IP: {target_ip} with Scan Type: {scan_type}")

launch_scan("10.0.0.1")        # Falls back to 'SYN'
launch_scan("10.0.0.2", "UDP")  # Overrides to 'UDP'

2. Variable-Length Positional Arguments (*args)
When the total count of inputs is unknown, *args packs all incoming elements into a Tuple.


def add_mass_targets(*targets):
    # 'targets' is handled as a Tuple inside the function
    for target in targets:
        print(f"[+] Target Registered: {target}")

add_mass_targets("phonics.edu", "api.phonics.edu", "admin.phonics.edu")


3. Keyword Arguments (kwargs)
When tracking dynamic named key-value mappings, kwargs packs arguments into a Dictionary. This is excellent for flexible loggers or vulnerability reports.

def build_report(**vuln_details):
    # 'vuln_details' is handled as a Dictionary inside the function
    for key, value in vuln_details.items():
        print(f"{key.upper()} -> {value}")

build_report(target="phonics.edu", cve="CVE-2024-XXXX", severity="CRITICAL")


🏁 Summary of Practical Lessons Learned
Operator Precision: Never use and for mutually exclusive single-variable checks; choose or.

Value Capturing: A return passes data silently in memory. Always explicitly wrap the call in a print() or store it in a variable to display it on screen.

Loop Variable Scope: Keep singular and plural object names clean during list/tuple iterations to prevent data dumping bugs.
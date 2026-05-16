# 🎛️ Control Flow & Logic Building in Python

Control Flow is how a program decides which path to take based on conditions. Instead of running code blindly from top to bottom, we give our scripts a "brain" to make decisions based on real-world inputs.

---

## 1. Conditional Statements (`if-elif-else`)

In Python, we use `if`, `elif` (else if), and `else` to evaluate conditions. This is extremely useful in automation (e.g., checking HTTP response codes during recon).

* **`if`**: The initial condition check.
* **`elif`**: Checks another condition if the previous ones were false.
* **`else`**: The fallback option if no conditions are met.

---

## 2. Logical Operators

We combine multiple conditions using logical operators:
* `and`: Returns True if **both** conditions are true.
* `or`: Returns True if **at least one** condition is true.
* `not`: Reverses the boolean result (True becomes False).

---

## 3. Practical Cyber Security Scenarios

Here is how Control Flow is used to build security automation and decision-making scripts:

### 🔒 Scenario 1: Password Strength Validator
Uses **nested `if-else`** statements and the `len()` function to analyze password length and complexity.
* If length is $\ge 8$ characters, it checks for specific complexity characters (like `_`).
* Categorizes passwords into **Strong**, **Medium**, or **Short**.

### 🚨 Scenario 2: Firewall Port Alerter
Uses **multiple `elif` statements combined with logical operators (`and` / `or`)** to flag exposed critical services.
* Standard web traffic (Ports 80/443) is marked normal.
* External access attempts to sensitive administrative ports like **SSH (22)** or **RDP (3389)** instantly trigger a `[🚨] CRITICAL ALERT`.

### 🛡️ Scenario 3: WAF Block Simulator
Simulates a Web Application Firewall (WAF) threshold mechanism.
* If a scanner generates high traffic (`request_count > 100`) OR uses signature tools (`user_agent == "BurpSuite"`), the script triggers an automatic temporary IP blacklist (`403 Forbidden`).

---

## 4. Loops & Loop Control (`break` & `continue`)

Loops are used to execute a block of code repeatedly.

* **`for` loop**: Used to iterate over a sequence (like a list, tuple, or a range of numbers).
* **`break`**: Terminates the loop immediately when a specific condition is met.
* **`continue`**: Skips the current iteration and jumps directly to the next one.

### 📝 Logic Code Snippet
```python
# Stops running completely when it hits 5
for number in range(1, 11):
    if number == 5:
        break
    print(number)

# Skips number 3 and prints the rest
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
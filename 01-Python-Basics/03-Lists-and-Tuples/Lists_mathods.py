fruits = ["Apple", "Banana", "Mango"]

# 1. append() - List ke end mein item add karta hai
fruits.append("Orange")

# 2. insert() - Kisi specific position (index) par item daalta hai
fruits.insert(1, "Pineapple") # Index 1 par Pineapple aa jayega

# 3. remove() - Kisi specific item ko delete karta hai (naam se)
fruits.remove("Banana")

# 4. pop() - Last item ko nikaal deta hai (ya index se nikaalta hai)
popped_item = fruits.pop() 

# 5. sort() - List ko alphabetical order mein set kar deta hai
fruits.sort()

print(f"Final List: {fruits}")
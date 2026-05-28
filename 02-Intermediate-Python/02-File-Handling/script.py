# # Basic Method (Traditional Way)
# file = open("Subdomain.txt", "r") # 'r' means read mode
# content = file.read()
# print(content)
# file.close() # Isko bhoolna mat!



# Humne spelling 'Subdoamin' se badal kar 'Subdomain' kar di hai
with open("Subdomain.txt", "r") as file:
    # readlines() se har domain alag-alag list mein aayega
    domains_list = file.readlines() 
    
print("Raw List:", domains_list)


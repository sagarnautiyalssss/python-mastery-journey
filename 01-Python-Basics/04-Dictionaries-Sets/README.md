# 📖 Dictionaries and Sets in Python

1. Dictionaries (Key-Value Pairs) 

Dictionarie is a collection that is used of keys an paires. In dict not using indexing like 0, 1, 2, 3, 4 only using key paires

   .Syntax: hacker = {"OS": "Kali", "IP": "1.1.1.1"}

   .Unique Keys : In Dict we can't create duplicate kyes, If we have 
    duplicate keys in dict then his overwrite the old value change and print new value 

   .Nested Data: We can also create a list inside the dictonarie 

   # example :- 
               data = {
                "name" = ["sagar", "Nautiyal", "Kiran Sharma"],
                "age" = [20, 21, 22],
                "Mb" = [8077, 8090, 212]
               }

2. Sets (The Duplicate Remover)    

Set is unordered collection he stored only uniques elements. Its automatic Remove the dplicate elements 

# Syntax: my_set = {1, 2, 2, 3} -> Output: {1, 2, 3}
  
    # example :- 
              mySet = {12, 11, 22, 11, 22, 1, 6}
              
              output = {12, 11, 22, 1, 6}

Use Case: When we have to remove the duplicat elements into the list so we can use of set he automatic remove all duplicate elements into the list 
            
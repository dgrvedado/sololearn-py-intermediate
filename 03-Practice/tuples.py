"""
You are given a list of contacts, where each contact is represented by a tuple, with the name and age of the contact.

Complete the program to get a string as input, search for the name in the list of contacts and output the age of the contact in the format presented below:

Sample Input

John

Sample Output 

John is 31 

If the contact is not found, the program should output "Not Found".
"""
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
]

def search_contact(search):
    for n in contacts:
        if search in n:
            return n
    return False
 
search = input()
found = search_contact(search)

if found == False:
    print("Not Found")
else:
    print(search + " is " + str(found[1]))



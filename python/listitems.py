# Small test for integrated python functions, and parsing and distributing lists

# Defining the function
def convertlist(n):
    list = n.split(", ")

    print("---")
    print("You have ", len(list), "items in the list.")
    print("---")
    for i in list:
        print(i)


# Getting input and calling the function
input = input("What items do you have? (separate by a comma and a space)")
convertlist(input) 

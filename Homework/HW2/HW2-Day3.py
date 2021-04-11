d = {"admin":"admin"}
print("Welcome!")
username = input("Enter your username: ")
password = input("Enter your password: ")
for k,v in d.items():
    if (k != username and v == password):
        print(" ")
        print("xxXxx Wrong username! xxXxx")
    elif(k == username and v != password):
        print(" ")
        print("xxXxx Wrong password! xxXxx")
    elif(k != username and v != password):
        print(" ")
        print("xxXxx Wrong username and password! xxXxx")
    else:
        print(" ")
        print("Congratulations")
        print("Login successful!", u'\u2713')
        



"""
for k,v in d.items():
    print("########################")
    print("#######--HINT--#########")
    print("########################")
    print("    username: ", k)
    print("    password: ", v)
    print("########################")
"""

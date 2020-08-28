import os
os.system("cls")
name=input("Enter your name : ")
def greet(name):
    """This function greets people"""
    print("Hello",name.capitalize(),"nice to meet you.\n")
    return greet

name_greet=greet(name)
print(greet.__doc__)    #optional
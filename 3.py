names=["ali","ahmed","mona"]
passwords=["123","0000",""]
print("welcom to our programme please write down your information to see our secret ")
x= input("please enter your user_name\n")
def search(x):
    for i in range (len(names)):
        if names[i]==x:
            return i
if search(x):

    if passwords[search(x)]=="":
        new_password=input("you did not assigne password for this account write the new password ")
    else:
        y = input("please enter the password ")
        if passwords[search(x)] ==y:
            print("our sescret that ibrahim donot like the fish ")
        else:
            print("wrong password ")
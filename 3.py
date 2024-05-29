names=["ali","ahmed","mona"]
passwords=["123","0000",""]
print("welcom to our programme please write down your information to see our secret ")

def search(x):
    for i in range (len(names)):
        if names[i]==x:
         return i
x= ""
while True:
    descision=input("please tell me what you want to make change the password press 1 or login press 2 \n")
    if descision=="2":
        x = input("please enter your user_name\n")
        index=search(x)
        if passwords[index]=="":
            new_password=input("this is an empty password please write a password  ")
            passwords[index]=new_password
        else:
            y= input("please enter the password ")
            if y ==passwords[index]:
                 print("the secret is one ")
            else:
                print("wrong password ")
    else:
        user=input("enter your user_name ")
        i=search(user)
        y=passwords[i]
        n=input("please enter your old password \n")
        if n ==y:
            new=input("write the new password ")
            passwords[i]=new


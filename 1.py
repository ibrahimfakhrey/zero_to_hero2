# x= input("please enter your name \n ")
# if x=="ibrahim":
#     print("welcom")
# else:
#     print("not welcom")

#task number two to make calculator


x=int(input("please enter the first number \n"))
y =int(input("please enter the second number \n"))
def sum (x,y):
    return x+y


def minus(x,y):
    return x-y
choice=input("please tell me what you want to make sum or minus \n")
if choice =="sum":
     print(sum(x,y))
elif choice =="minus":
    print(minus(x,y))
else:
    print("somthing went wrong ")

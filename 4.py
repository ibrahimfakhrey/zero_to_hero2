import random

data={
    "hi":"a word we say it in the early morning",
    "by":" a word we say it to end the conversation "
}
users={
    "ibrahim":[
        "1111","admin"
    ],
    "mohamed":["0000","user","pay"]
,
    "salah":["1234","teacher"]

}
def generate_password():
    capital_letters = [chr(i) for i in range(65, 91)]

    # List of small letters from a to z
    small_letters = [chr(i) for i in range(97, 123)]

    # List of numbers from 1 to 10
    numbers = ["0","1","2","3","4","5","6","7","8","9","10"]

    # List of common symbols
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', ':', ';', '"',
               "'", '<', '>', ',', '.', '?', '/']

    password=""

    for i in range(3):
        password+=random.choice(capital_letters)
        password += random.choice(small_letters)
        password += random.choice(numbers)
        password += random.choice(symbols)
    return password

print(generate_password())
while True:
    x=input("please enter your username\n")
    if x in users:
        password=users[x][0]
        role=users[x][1]
        user_password=input("please give me the password ")
        if password==user_password:
            if role =="user":
                target=input("if you want to generate an new password for your press 1 \n")
                if target =="1":
                  new_password=generate_password()
                  print(f" your new_password is {new_password}")
                  users[x][0]=new_password


                else:
                    word=input("please enter the word \n")
                    if word in data:
                        print(data[word])
                    else:
                        print(f" i donot know what is the meaning of {word}")
            if role=="teacher":
                new_word=input("if you want to add an new word please writ it \n")
                if new_word in data:
                    print(f"this word is inside the dictionary and it is {data[new_word]}")
                else:
                    new_def=input(f"ok what is the definiion of {new_word} \n")
                    data[new_word]=new_def
            if role=="admin":
                target=input("please give me the username you want to change \n")
                if target in users:
                    his_role=users[target][1]
                    print(f"i found that he is {his_role}")
                    new_role=input("tell me what you want for him admin , teacher,users \n")
                    his_role=new_role
                    new_choice =input("if you want to change the password for the user press one \n")
                    if new_choice=="1":
                        users[target][0]=generate_password()
                        print(f"the password for {target} changed to {users[target][0]}")



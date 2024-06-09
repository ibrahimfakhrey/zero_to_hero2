data={
    "hi":"a word we say it in the early morning",
    "by":" a word we say it to end the conversation "
}
users={
    "ibrahim":[
        "1111","admin"
    ],
    "mohamed":["0000","user"]
,
    "salah":["1234","teacher"]

}

while True:
    x=input("please enter your username\n")
    if x in users:
        password=users[x][0]
        role=users[x][1]
        user_password=input("please give me the password ")
        if password==user_password:
            if role =="user":
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


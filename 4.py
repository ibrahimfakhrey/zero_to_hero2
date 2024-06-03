data={
    "hi":"a word we say it in the early morning",
    "by":" a word we say it to end the conversation "
}
# for key in data:
#     print(key)
#     print(data[key])

while True:
    x=input("please enter the word you are searching for ")
    if x in data:
        print(data[x])
    else:
        new_valu=input("it seemes for me that i donot have this word  add it to me  write the value of this word ")
        data[x]=new_valu

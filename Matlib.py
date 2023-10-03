print("       MATLIB GAME       ")
print(" 1.Computer\n 2.President")
choice=int(input("Enter choice: "))
if(choice==1):
#computer
    noun1=input("Noun: " )
    p_noun1=input("Plural Noun: " )
    verb1=input("Verb: ")
    verb2=input("Verb: ")
    BP=input("A body part: ")
    adj1=input("Adjective: ")
    P_noun2=input("Plural Noun: ")
    adj2=input("Adjective: ")
    TMC=f"today, every student has a computer small enough to fit into his {noun1}.\
    He can solve any math problem by simply pushing computer's little {p_noun1}.\
    Computers can add,multiply,divide, and {verb1}. They can also {verb2} better than\
    a human. Some computers are {BP}. Others have a/an {adj1} screen that shows all \
    kinds of {P_noun2} and {adj2} figures."
    print(TMC)
elif(choice==2):
#president
    Name=input("Name: ")
    age=input("Age: ")
    adj1=input("Adjective: ")
    color1=input("Color: ")
    noun1=input("Noun: ")
    food1=input("Food: ")
    noun2=input("Noun: ")
    verb1=input("Verb: ")
    clothing=input("Cloth: ")
    adj2=input("Adjective: ")
    celeb=input("Celebrity: ")
    pres=f"My name is {Name} and i am {age} years old. If i were president,i'd do \
    a whole bunch of {adj1} things: \
    \n 1. I would drive the biggest {color1} car in the country. And that\
    car would go faster than any other {noun1} in the world!\
    \n 2.Everyone would eat pepperoni {food1} for dinner.\
    \n 3.I would live in the Statue of {noun2} and build a {verb1} pool at her feet\
    \n 4. I would wear a/an {clothing} on my head, and everyone would\
    say i look {adj2} like {celeb}."
    print(pres)
else:
    print("wrong choice")

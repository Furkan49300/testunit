import datetime

h=datetime.datetime.now().hour

if 18>h>5:
    print("bonjour, hello")
else:
    print ("bonsoir, goo evening")

while True:
    x=str(input("ecrivez un mot ou 'quitter' pour quitter: "))

    if x=="quitter":
        break

    if x[::-1] == x:
        print("bien dit!")
    else:
        print(x)
print("au revoir, good bye")

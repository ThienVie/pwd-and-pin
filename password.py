import secrets
import string as s
p = "pin"
pss = "password"

chg = s.ascii_uppercase
chk = s.ascii_lowercase
chzah = s.digits
chzei = s.punctuation
f = False

#---------------------------
def end():
    print("")
    print("----------------------")
    print("")
    print(f"Your {l} is:    {pwd}")
    print("")
    print("----------------------")
    print("")
#---------------------------
print("")
print(f"Options:    {p}    {pss}")
print("")

while f == False:
    c = str(input("What is it: "))
    if c == pss:
        f = True
    elif c == p:
        f = True
    else:
        print("This is not an option")
        print("")
pwd = ""
    

if c == p:
    ch = chzah
    a = 4
else:
    d = False
    while d == False:
        ch = chg + chk + chzah + chzei
        try:
            a = int(input("How long has it to be: "))
            break
        except ValueError:
            print("")
            print("! = ValueError")
            print("You wrote something wrong.")
            print("")
for _ in range(a):
    pwd += secrets.choice(ch)
l = c

if a <= 3:
    print("Erm...")
    print("Can you explain why you choose 1, 2, or 3?")
    print("I really don't get it.")
    print("but still I wish you a happy day. <3")
    print("")
    end()
elif a == 0:
    print("")
    print("----------------------")
    print("")
    print("This is really sad, that you choose zero, :(")
    print("but still I wish you a happy day. <3")
    print("If today is your birthday, then I wish you a happy birthday.")
    print("")
    end()
<<<<<<< HEAD

else:
    print()
    end()
=======
    print("I wish you a happy day. <3")
    print("If today is your birthday, then I wish you a happy birthday.")
    print("")
>>>>>>> 884012717c8db5f8da9f4dd22c02e8578e1a7dec

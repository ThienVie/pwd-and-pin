import secrets
import string as s

chg = s.ascii_uppercase
chk = s.ascii_lowercase
chzah = s.digits
chzei = s.punctuation
f = False
print("I don't know if it  is randomly or not, but here it is.")
#---------------------------
def end():
    print("")
    print("----------------------")
    print("")
    print(f"Your password is:    {pwd}-{hallo}-{sub}")
    print("")
    print("----------------------")
    print("")
#---------------------------

hallo = ""
pwd = ""
sub = ""
ch = chg + chk + chzah

for _ in range(6):
    pwd += secrets.choice(ch)

for _ in range(6):
    hallo += secrets.choice(ch)

for _ in range(6):
    sub += secrets.choice(ch)

end()

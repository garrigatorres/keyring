import keyring

f = open("users", "r")
for x in f:
  print("The password for",x.rstrip(),"is :",keyring.get_password("new_keyring", x.rstrip()))

f.close()

import keyring

f = open("usuaris", "r")
for x in f:
  print("El password de",x.rstrip(),"és :",keyring.get_password("keyring_nou", x.rstrip()))

f.close()

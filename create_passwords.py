import random
import keyring

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!£$%^&*(`)"
password_len = 8

f = open("users", "r")
for x in f:
  password  = ""
  for y in range(0,password_len):
    password_char = random.choice(chars)
    password = password + password_char
  keyring.set_password("new_keyring", x.rstrip(), password)

f.close()

#   a212_rsa_encrypt.py
import rsa as rsa

key = (input("Enter the Encryption Key: " ))
while key.isdigit() == True:
  mod_value = (input("Enter the Modulus: " ))
  break

else:
  print("Must insert Number.")
  key = (input("Enter the Encryption Key: " ))

while mod_value.isdigit() == True:
  plaintext = input("Enter a message to encrypt: ")
  break

else:
  print("Must insert Number.")
  mod_value = (input("Enter the Modulus: " ))


encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
print("Encrypted Message:", encrypted_msg)


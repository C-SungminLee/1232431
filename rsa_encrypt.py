#   a212_rsa_encrypt.py
import rsa as rsa

key = (input("Enter the Encryption Key: " ))
while key.isdigit() != True:
  print("Must insert Number.")
  key = (input("Enter the Encryption Key: " ))

else:
  mod_value = (input("Enter the Modulus: " ))


while mod_value.isdigit() != True:
  print("Must insert Number.")
  mod_value = (input("Enter the Modulus: " ))
  

else:
  plaintext = input("Enter a message to encrypt: ")
  


encrypted_msg = rsa.encrypt(int(key), int(mod_value), plaintext)
print("Encrypted Message:", encrypted_msg)


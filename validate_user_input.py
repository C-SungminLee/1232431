#   a212_rsa_encrypt.py

# This program validates input from a user
'''
isalpha. This method returns True if all characters in the string are alphabetic (a-z or A-Z) 
and there is at least one character in the string. Otherwise, it returns False.

'''
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


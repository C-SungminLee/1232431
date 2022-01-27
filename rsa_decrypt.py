#   a212_rsa_decrypt.py
import rsa as rsa

key = (input("Enter the Decryption Key: " ))
while key.isdigit() != True:
  print("Must insert Number.")
  key = (input("Enter the Decryption Key: " ))

else:
  mod_value = (input("Enter the Modulus: " ))


while mod_value.isdigit() != True:
  print("Must insert Number.")
  mod_value = (input("Enter the Modulus: " ))
  

else:
  encrypted_msg = input("What message would you like to decrypt (No brackets): ")



#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(int(key),int(mod_value) , msg))

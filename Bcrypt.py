import bcrypt
import time

def gang():
    input("Enter a password: ")
gang() 

password = b'gang()'

start = time.time()
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)
end = time.time()  

print(salt)
print(hashed)

if bcrypt.checkpw(password, hashed):
    print("Passwords Match")
else:
    print("Passwords do not match")

print("This process took " + str(end - start) + " seconds.")

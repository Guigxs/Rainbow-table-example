from passlib.hash import nthash
import random

val = "abcdefghijklmnopqrstuvwxyz"
with open("sol.txt", "w") as sol:
    with open("password.txt", "w") as file:
        for i in range(5000):
            password = ""
            for j in range(3):
                password += random.choice(val)
                
            
            sol.write(password+"\n")

            file.write(nthash.hash(password)+"\n")
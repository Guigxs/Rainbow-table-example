from passlib.hash import nthash
from pymongo import MongoClient
import re

def new_password_entry():
    while(1):
        print("\n---Password configuration---")
        user_name = input("User_name : ")
        password1 = input("Password : ")
        password2 = input("Confirm Password : ")
        if( password1 == password2 ):
            if re.match(r'[a-z]{3}', password1 ):
                password = nthash.hash(password1)
                return (user_name,password)
            else:
                print("\nPassword must have 3 letters in lowercase")
        else:
            print("\n  Les deux mots ne sont pas les mêmes")


def addToDB(user,password):
    try:
        client = MongoClient("mongodb://rainbowUser:rainbowUser123456@cluster0-shard-00-00.m9mex.mongodb.net:27017,cluster0-shard-00-01.m9mex.mongodb.net:27017,cluster0-shard-00-02.m9mex.mongodb.net:27017/password?ssl=true&replicaSet=atlas-g163gx-shard-0&authSource=admin&retryWrites=true&w=majority")
        db =client.password
        db.passwords.insert_one({"user":user,"password":password})
        print( "======> Succesfuly added")
    
    except:
        print("Failed to Add to DB")


while(1):
    user, password = new_password_entry()
    addToDB(user,password)
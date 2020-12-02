from passlib.hash import nthash
from pymongo import MongoClient

def toChar(val):
    while val >= 123 or val < 97:
        if val < 97:
            val += 26
        else:
            val -= 26
        
    return chr(val)


def searchPassword(firstKey, targetHash):
    hash = nthash.hash(firstKey)
    newHash = hash

    if hash == targetHash:
        print("Password found: {}".format(firstKey))
        return True

    for i in range(0, 21, 3):
        chunck1 = int(newHash[i:i+3], 16)
        chunck2 = int(newHash[i+1:i+4], 16)
        chunck3 = int(newHash[i+2:i+5], 16)

        newWord = "{}{}{}".format(toChar(chunck1), toChar(chunck2), toChar(chunck3))

        newHash = nthash.hash(newWord)

        if (targetHash == newHash):
            print("Password found: {}".format(newWord))
            return True

    return False

def reduce(newHash, reduceNumber):
    if reduceNumber == 7:
        return newHash

    for i in range(reduceNumber*3, 21, 3):
        chunck1 = int(newHash[i:i+3], 16)
        chunck2 = int(newHash[i+1:i+4], 16)
        chunck3 = int(newHash[i+2:i+5], 16)

        newWord = "{}{}{}".format(toChar(chunck1), toChar(chunck2), toChar(chunck3))

        newHash = nthash.hash(newWord)

    return newHash

def check(target, rainDict):
    i = 7

    while i >= 0:
        reduceHash = reduce(target, i)

        for firstKey, value in rainDict.items():
            if reduceHash == value:
                # print("Hash found ! Searching password...")

                if searchPassword(firstKey, target): # Une fois le hash trouvé, on cherche le mdp
                    return True
        i-=1 

    print("No password found !")
    return False




client = MongoClient("mongodb://rainbowUser:rainbowUser123456@cluster0-shard-00-00.m9mex.mongodb.net:27017,cluster0-shard-00-01.m9mex.mongodb.net:27017,cluster0-shard-00-02.m9mex.mongodb.net:27017/password?ssl=true&replicaSet=atlas-g163gx-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.password
users = db.passwords.find()

with open ("MyRainbowTable.txt") as file:
    rainDict = {}
    for line in file:
        code, hash = line.split(":")
        rainDict[code] = hash[0:-1]

for user in users:
    db_username = user["user"]
    db_hash = user["password"]
    targetHash = db_hash
    print(f"\n\nChecking for {db_username}...")
    check(targetHash, rainDict)
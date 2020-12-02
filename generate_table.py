from passlib.hash import nthash

def toChar(val):
    while val >= 123 or val < 97:
        if val < 97:
            val += 26
        else:
            val -= 26
        
    return chr(val)

with open ("MyRainbowTable.txt", "w") as RT:
    with open ("sol.txt", "r") as sol:
        solList = []
        for lineSol in sol:
            solList.append(lineSol[0:-1])
        with open ("password.txt", "r") as file:
            hashList = []
            hashSet = set()

            for line in file:
                hashList.append(line[0:-1])
                hashSet.add(line[0:-1])

            for h in range(len(hashList)):
                text = "New hash chain : {}".format(hashList[h])
                newHash = hashList[h]

                for i in range(0, 21, 3):
                    # print(newHash)
                    # print(newHash[i:i+3])
                    # print(newHash[i+1:i+4])
                    # print(newHash[i+2:i+5])

                    chunck1 = int(newHash[i:i+3], 16)
                    chunck2 = int(newHash[i+1:i+4], 16)
                    chunck3 = int(newHash[i+2:i+5], 16)
                    
                    newWord = "{}{}{}".format(toChar(chunck1), toChar(chunck2), toChar(chunck3))
                    newHash = nthash.hash(newWord)
                    
                    hashSet.add(newHash)
                    text += " - {} - {}".format(newWord, newHash)

                RT.write("{}:{}\n".format(solList[h], newHash))
                text += "\n"
                print(text)


print("Covering " + str(len(hashSet)) + " passwords over 17576!")



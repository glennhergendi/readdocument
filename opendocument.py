def opening_function():
    f = open("believer.txt", "r")
    data = f.read()
    print(data)
    f.close
opening_function()

#calculate the number of letters
def characters_function():
    f = open("believer.txt", "r")
    data = f.read()
    c = len(data) #calculates the number of letters
    print("number of letters: ",c)
    f.close()
characters_function()

def lowerletter_function():
    f = open("believer.txt", "r")
    data = f.read()
    cnt = 0
    for ch in data:
        #checks the letter if it is lowercase
        if ch.islower():
            cnt += 1
    f.close()
    print("no. of lowercase letters: ", cnt)
lowerletter_function()

def upperletter_function():
    f = open("believer.txt", "r")
    data = f.read()
    count = 0
    for x in data:
        if x.upper():
            count += 1
    f.close()
    print("no. of uppercase letters:", count)
upperletter_function()

def findS_function():
    f = open("believer.txt", "r")
    data = f.read()
    counts = 0
    for i in data:
        if i[0] == "S":
            counts += 1
    f.close()
    print("no. of letter S:", counts)
findS_function()

def nmbr_words_function():
    f = open("believer.txt", "r")
    data = f.read()
    count = 0
    ws = input("enter word to find: ")
    word = data.split()
    #looping to find lowercase
    for w in word:
        if ws.lower() in w.lower():
            count += 1
    f.close()
    print(ws, "found", count, "times in the file")
nmbr_words_function()
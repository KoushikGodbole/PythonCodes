
def missingword(s, t):
    i = 0
    tempS = s.split()
    tempT = t.split()
    Sdict = dict.fromkeys(tempS,1)
    for i in range(0,len(tempT)):
        if tempT[i] in Sdict:
            del(Sdict[tempT[i]])
    print(Sdict.keys())





str1 = "I am using HackerRank to improve programming"
str2 = "am HackerRank to improve"
missingword(str1,str2)
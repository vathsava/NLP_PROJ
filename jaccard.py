from __future__ import division

def calcJaccard(stringA,stringB):
 #   print stringA
    str2 = stringA.rstrip()
    str3 = str2.replace("?","")
    wordsA=stringA.split(" ");
    wordsB=stringB.split(" ");
    count=0;
    
    for a in wordsA:
        for b in wordsB:
            if a==b :
                count+=1;
   # print count
    return(count/(len(wordsA)+len(wordsB)))
           
#print calcJaccard(stringA, stringB)


    
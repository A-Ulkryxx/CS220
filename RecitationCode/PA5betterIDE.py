from itertools import permutations as permut

def make_postage(money) :
    
    if(((money % 5) == 0) and ((money % 3) == 0)): #if evenly divisible by both 5 and 3, prioritive divisor 3, return (0,numthrees)
        return (0,int(money/3))
    if ((money % 5) == 0):                         #if divisible by 5, return (numfives,0)
        return (int(money/5),0)
    if((money % 3) == 0):                          #if divisible by 3, return (0,numthrees)
        return (0,int(money/3))
    
    numThrees = money // 3
    
    while( ( (money - (numThrees * 3) ) % 5 ) != 0 ):
        numThrees = numThrees - 1
    
    numFives = (money - (numThrees * 3)) // 5
    
    return (numFives, numThrees)


def permutations(s):
    return set(permut(s))
#    if (len(s) == 0):
#        return ()
#    if (len(s) == 1):
#        return {s}

#    perm =[]

#    for i in range(len(s)):
#        first = s[i]
#        work = s[0:1]
#        todo = s[i +1:]
#        remain = work + todo
#        perm.append(())
#        permutations(remain)
#    return perm  

print(permutations((1,2)))
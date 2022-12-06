'''
     PA2: Boolean functions and truth-table inputs
     -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

For PA2 you will implememnt a number of Boolean functions,
such as implies, nand, etc.

a) Boolean functions
You are provided with a set of Boolean functions to implement.
You will create the bodies for these 2 parameter functions, such that 
they return the appropriate Boolean value (True or False). 
The formal parameters are always p and q (in that order)

Notice the difference between npIMPnq and nqIMPnp:
In npIMPnq you return not p implies not q (not first 
param implies not second param), for example 
  npIMPnq(True,False) returns True.

In nqIMPnp you return not q implies not p (not second 
param implies not first param), for example
  nqIMPnp(True,False) returns False.

b) Truth-table inputs


Two functions are provided: run(f) and main, so that you can test 
your code.

  python3 PA2.py <fName> tests your Boolean function <fName>
  python3 PA2.p=y tt <n> tests your function make_tt_ins(<n>)
 
'''


import sys
from copy import copy

# p implies q
def implies(p, q):
    if((p == True) and (q == False)):
        return False
    else:
        return True

# not p implies not q
def npIMPnq(p,q):
    if(((not p) == True) and ((not q) == False)):
        return False
    else :
        return True

# not q implies not p
def nqIMPnp(p,q):
    if(((not q) == True) and ((not p) == False)):
        return False
    else :
        return True

# p if and only if q
# equivalent to:  (p implies q) and (q implies p)
def iff(p, q):
    return (p == q) and (q == p)

# not ( p and q )
def nand(p, q):
   return (not(p and q))
        
# not p and not q
def npANDnq(p,q):
    return ((not p) and (not q))

# not ( p or q)
def nor(p, q):
    return not(p or q)

# not p or not q
def npORnq(p,q):
    return ((not p) or (not q))

'''The function make_tt_ins(n) will create all combinations of n Boolean variables. 
The output is in the form of a list, each element of which is a list with n
Boolean values.
For example, make_tt_ins(2) should return
[[False, False], [False, True], [True, False], [True, True]] '''

    #Written for n < 4 for all positive integers
def make_tt_ins(n):
    truthT = []
    if(n == 0):
        return truthT
    
    flags = n*[True]

    for i in range(2**n):
        truthT.append(copy(flags))
            #Changes least significant bit every iteration
        flags[n - 1] = not flags[n - 1]
        if(i % 2 == 1):  
                #Changes second to least significant bit every iteration 
            flags[n - 2] = not flags[n - 2]
        if( n >= 3):
            if(i % 4 == 1):  
                    #Changes third to least significant bit
               flags[n - 3] = not flags[n - 3]
            if(i % 8 == 1):
                    #Changes most significant bit
                flags[n-4] = not flags[n-4]
        
        
    return truthT

#provided
def run(f):
  print("  True,True  : ", f(True,True)) 
  print("  True,False : ", f(True,False))  
  print("  False,True : ", f(False,True))
  print("  False,False: ", f(False,False))
  print()
      
#provided
if __name__ == "__main__":
  print("program", sys.argv[0])
  f1 = sys.argv[1]
  print(f1)
  if(f1 == "implies"):
    run(implies)
  if(f1 == "iff"):
    run(iff)
  if(f1 == "npIMPnq"):
    run(npIMPnq)
  if(f1 == "nqIMPnp"):
    run(nqIMPnp)
  if(f1 == "nand"):
    run(nand)
  if(f1 == "nor"):
    run(nor)
  if(f1 == "npANDnq"):
    run(npANDnq)
  if(f1 == "npORnq"):
    run(npORnq)
  if(f1 == "tt"):
    print(make_tt_ins(int(sys.argv[2])))

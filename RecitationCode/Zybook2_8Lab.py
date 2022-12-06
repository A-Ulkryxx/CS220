def set_new() :
    """Return a new set"""
    return []


def set_remove(s, value): 
    """Remove the given value from the set s"""
    # perform some type checking to see that the user
    # has provided the right kind of input:
    if type(s)!=type([]) :
        raise ValueError
    # we can simply use the "remove" method of a list:
    while(set_membership(s, value)):
        s.remove(value)
    # to be complete before returning we should make sure there are no duplicates - not shown
    for i in s:
        counter = 0;
        for j in s:
            if ((i == j) and (counter != 0)):
                s.remove(s[j])
                
            if (i == j):
                counter = counter + 1 
            
    return s
    

def set_union(s1, s2) :
    """Return the union of sets s1 and s2 as a list"""
    if type(s1)!=type([]) or type(s2)!=type([]):
        raise ValueError
        
    s1.sort()
    s2.sort()
    s3 = []   
    
    for i in s2:
        if (not set_membership(s3, i)):
            s3.append(i)        
    for i in s1:
        if (not set_membership(s3, i)):
            s3.append(i)
    
    return  s3


def set_intersection(s1, s2) :
    """Return the intersection of sets s1 and s2 as a list"""
    if type(s1)!=type([]) or type(s2)!=type([]):
        raise ValueError
        
    s1.sort()
    s2.sort()
    s3 = []
    
    for j in s2:
        if ((set_membership(s1, j)) and (not set_membership(s3, j))):
            s3.append(j)
                
    return s3

def set_membership(s, value):
    """Return True if value is in the set s, and False otherwise"""
    if type(s)!=type([]) :
        raise ValueError 
        
    for i in s:
        if (value == i):
            return True
        
    return False

def set_equals(s1, s2) :
    """Return True if the sets s1 and s2 have exactly the same elements"""
    if type(s1)!=type([]) or type(s2)!=type([]):
        raise ValueError   
        
    s1.sort()
    s2.sort()
    
    return s1 == s2


def set_difference(s1, s2) :
    """Return the set difference of s1 and s2"""
    if type(s1)!=type([]) or type(s2)!=type([]):
        raise ValueError
      
    s3 =[]        
    for j in s1:
        if ( (not set_membership(s3, j)) and (not set_membership(s2, j)) ):
            s3.append(j)
    
    return s3


def is_subset(s1, s2) :
    """Return True if s1 is a subset of s2"""
    if type(s1)!=type([]) or type(s2)!=type([]):
        raise ValueError
        
    s1.sort()
    s2.sort()
        
    if(len(s1) == 0):
        return True
      
    flag = True
    for i in s1:
        if(not set_membership(s2, i)):
            flag = False
            
    return flag


def is_proper_subset(s1, s2) :
    """Return True if s1 is a proper subset of s2"""
    if type(s1)!=type([]) or type(s2)!=type([]):
        raise ValueError
        
    s1.sort()
    s2.sort()
    
    if(len(s1) == 0):
       return True
   
    if (len(s1) < len(s2)):
        flag = True
        for i in s1:
            if(not set_membership(s2, i)):
                flag = False
                
        return flag
    
    return False
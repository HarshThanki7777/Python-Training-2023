"""
Difference between list and tuple

=> List Is a Collection of datatype similar and dis-similar data elements
list which is represent by[] braces when tuple is a collection data type and which contain similar and di-similar

=> List which is mutable (we can change it value) - we can perform append, insert, remove all operations but same way

=> tuple is a immutable (we can't change it value ) we can't perform append insert, remove operations

=> list is slower than tuple

=> tuple is faster than list


"""

t= (1,2,3,4)
print(t)


for i in t:
    print(i)
    
    print(len(t))
    
    t1 = ("Python", "Java", "Android")
    
    l1 = list(t1) #convert tuple into list
    
    l1.append("node.js")
    
    t1 = tuple(l1) #convert list into tuple
    
    print(t1)
    
    #---
    t = ("Python")
    print(type(t)) #Type Is an InBuilt Function Which Is Used To Check Which Type Of Value Store In variable.......
    
    """
    Set : set is a collection data type
        
        set which is immutable, unorderable, unindexable
        
        set does not contain duplicates elements 
        set which is represent by{}    
    
    
    """
    
    s = {10,20,30}
    print(s)
    
    s1 = {"java","python","android","php","node.js","android","java"}
    print(s1)
    
    #imp : remove duplicate elements from list or find unique values from the list
    l1 = [12,23,54,12,23,7]
    s = set(l1) #convert into set
    print(s)
    
    #imp : remove duplicate elements from list or find unique values from the list without using set
    
    unique_list = []
    
    l1 = ["java","python","php","java","php"]
    
    for i in l1:
        if i not in unique_list:
            unique_list.append(i)
            
    print(unique_list)
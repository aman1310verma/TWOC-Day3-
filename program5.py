def intersection(lst1, lst2): 
    lst3 = [i for i in lst1 if i in lst2] 
    return lst3 
  
lst1=[]
lst2=[]
lst1 = input("Enter list 1") 
lst2 = input("Enter list 2") 
print(intersection(lst1, lst2)) 
def rm_Duplicate(str): 
    tl="" 
    for i in str: 
        if(i in tl): 
            pass
        else: 
            tl=tl+i 
        print("New string is :",tl) 
      
str=input("Enter string")
rm_Duplicate(str) 
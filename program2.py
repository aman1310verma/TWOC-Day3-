def pfun(strin, l=0):
    if(step == len(strin)):
        print("".join(strin),end=" ")
    for i in range(l,len(strin)):
        c_list = [j for j in strin]
        c_list[l],c_list[i] = c_list[i],c_list[l]
        perm(c_list,l+1)

        
str1= input("Enter a string:")        
print("\nPrinting..")
pfun(str1)        
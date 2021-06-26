l = [1, 3, 5,7]
n = int(input("enter numbers of next odd number you want to print:"))
d = l[-1]  #7
for i in range(n):           
    e = d+2                #7+2
    l.append(e)      #9
    d = l[-1+i]        #11
print(l)
print(d)

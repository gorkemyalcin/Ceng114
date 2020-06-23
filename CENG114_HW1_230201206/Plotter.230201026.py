#230201026 Ali Görkem Yalçın
#100000 took 48 minutes
#10000 takes 26 seconds
import numpy as np
import matplotlib.pyplot as plt

def lcg(modulus, a, c, seed):
    while True:
        seed = (a * seed + c) % modulus
        return seed
    
lista=[]
listb=[]
listc=[]
listx=[]

listavga=[]
listavgb=[]
listavgc=[]
listavgx=[]

listvarx=[]

count=0
avga=0
avgb=0
avgc=0
avgx=0

while count<100000:
    count = count + 1
    a = int(lcg(6,123,343,np.random.rand()))+1
    b = int(lcg(4,154,312,np.random.rand()))+1
    c = int(lcg(2,213,323,np.random.rand()))
    if c == 1:
        c = 1
    elif c == 0:
        c = -1
    x = a + b*c
    avga = ((count-1)*avga + a)/count
    avgb = ((count-1)*avgb + b)/count
    avgc = ((count-1)*avgc + c)/count
    avgx = ((count-1)*avgx + x)/count
    lista.append(a)
    listb.append(b)
    listc.append(c)
    listx.append(x)
    
    varx=0
    u=0
    sum=0
    
    for i in listx:
        u=u+i
    u=u/count
    
    for i in listx:
        sum=sum+((u-i)**2)
        
    if len(listx)==1: #to not get division by 0 error
        varx=0
    else:
        varx=sum/(len(listx)-1)
        
    
    listvarx.append(varx)
    listavga.append(avga)
    listavgb.append(avgb)
    listavgc.append(avgc)
    listavgx.append(avgx)
user_input=(input("Please press\n 1 for variable a\n 2 for variable b\n 3 for variable c\n 4 for variable x\n 5 for average of a\n 6 for average of b\n 7 for average of c\n 8 for average of x \n 9 for variance of x\n"))
if user_input==("1"):
    plt.hist(lista)
elif user_input==("2"):
    plt.hist(listb)
elif user_input==("3"):
    plt.hist(listc)
elif user_input==("4"):
    plt.hist(listx)
elif user_input==("5"):
    plt.hist(listavga)
elif user_input==("6"):
    plt.hist(listavgb)
elif user_input==("7"):
    plt.hist(listavgc)
elif user_input==("8"):
    plt.hist(listavgx)
elif user_input==("9"):
    plt.hist(listvarx)
#230201026 Ali Görkem Yalçın
import numpy as np
from matplotlib import pyplot as plt

# Part a (Inverse Transform Method)
U = []
Xa = []
av_Xa = []
vr_Xa = []

# Populate the given arrays.
### YOUR CODE HERE ###
count=0
avg_xa=0
u=0
while count<50000:
    count=count+1
    element_u=np.random.rand()
    element_xa=element_u**0.5
    U.append(element_u)
    Xa.append(element_xa)
    avg_xa= ((count-1)*avg_xa + element_xa)/count
    av_Xa.append(avg_xa)
    sum=0
    varx=0
    u=u+Xa[count-1]
    u=u/count
    for i in Xa:
        sum=sum+((u-i)**2)
            
    if len(Xa)==1: #to not get division by 0 error
        varxa=0
        vr_Xa.append(varxa)      
    else:
        varxa=sum/(len(Xa)-1)
        vr_Xa.append(varxa)
    u=u*count   
# Inspect the following plots.
plt.figure()
for i in range(len(Xa)):
    plt.plot([Xa[i],U[i]],[1,1.2])
plt.figure()
hU = plt.hist(U,100,alpha=0.5,normed=True)
hXa = plt.hist(Xa,100,alpha=0.5,normed=True)
plt.figure()
plt.plot(np.cumsum(hU[0]))
plt.plot(np.cumsum(hXa[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###

plt.figure()
plt.hist(av_Xa,100,normed=True)#avxa

plt.figure()
plt.hist(vr_Xa,100,normed=True)#varxa

# Part b (Rejection Method)
Xb = []
av_Xb = []
vr_Xb = []

# Populate the given arrays.
### YOUR CODE HERE ###
count=0
avg_xb=0
u=0
xb_quantity=0
while count < 50000:
    count=count+1
    T=np.random.rand()
    P=np.random.rand()
    if (T**2)/(P**2) > 1:
        element_xb=T
        Xb.append(element_xb)
        xb_quantity=xb_quantity+1
        
        u=u+Xb[xb_quantity-1]
        u=u/xb_quantity
        sum=0
        varxb=0
        avg_xb= ((count-1)*avg_xb + element_xb)/count
        av_Xb.append(avg_xb)

        for i in Xb:
            sum=sum+((u-i)**2)
            
        if len(Xb)==1: #to not get division by 0 error
            varxb=0
            vr_Xb.append(varxb)
            
        else:
            varxb=sum/(len(Xb)-1)
            vr_Xb.append(varxb)
        if (T**2)/(P**2) > 1:
            u=u*xb_quantity
# Inspect the following plots.
plt.figure()
hXb = plt.hist(Xb,100,normed=True)
plt.figure()
plt.plot(np.cumsum(hXb[0]))

# Plot the average and variance values.
### YOUR CODE HERE ###

plt.figure()
plt.hist(av_Xb,100,normed=True)#avxb

plt.figure()
plt.hist(vr_Xb,100,normed=True)#varxb


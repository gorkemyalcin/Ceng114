#230201026 Ali Gorkem Yalcin
import matplotlib.pyplot as plt
import numpy as np
import math

mleEstimators=[]     
momEstimators=[]
P=[]
count=0
X=[0.3 , 0.6 , 0.8 , 0.9]

while count<10000000:#inverse transform method
    count+=1
    P.append((np.random.rand()/2.4)**1.4)
    
def MoM(listx):
    sum=0
    for i in listx:
        sum=sum+i
    mean=sum/len(listx)
    estimator=mean/(1-mean)
    return estimator

def MLE(listx):
    sum=0
    for i in listx:
        sum=sum+(math.log(i))
    estimator=-len(listx)/sum
    return estimator
        
def mil(P,N):
    for i in range(100):
        sampleList=[]
        for i in range(N):#N=100k
            randIntIndex=(np.random.randint(0,10000))#make this 10mil
            sampleList.append(P[randIntIndex])
        
        momEstimators.append(MoM(sampleList))
        mleEstimators.append(MLE(sampleList))
    plt.figure()
    plt.hist(momEstimators,100,alpha=0.5)
    plt.hist(mleEstimators,100,alpha=0.5)

    mean=np.mean(momEstimators)
    var=np.var(momEstimators)
    print("\nFor N="+str(N)+" \nVariance of MoM estimators: "+ str(var) + " \nMean of the MoM estimators:: " + str(mean))
    
    mean=np.mean(mleEstimators)
    var=np.var(mleEstimators)
    print("\nVariance of MLE estimators: "+ str(var) + " \nMean of the MLE estimators:: " + str(mean))
    
print("\nQuestion.1a) Estimator for method of moments is "+ str(MoM(X))+"\n")
print("Question.1a) Estimator for most likelihood estimation is "+ str(MLE(X)))   
    
mil(P,1)
mil(P,2)
mil(P,3)
mil(P,4)
mil(P,5)
mil(P,10)
mil(P,50)
mil(P,100)
mil(P,500)
mil(P,1000)
mil(P,100000)


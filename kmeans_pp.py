import numpy as np
from numpy import genfromtxt
import pandas as pd
import sys
np.random.seed(0)

def checktype(str):
    try:
        bol=(int(str)==float(str))
        return not bol
    except:
        print("An Error Has Occurred")
        sys.exit(1)

#input
arglist=sys.argv
if len(sys.argv)==6:
    try:
        K=int(arglist[1])
    except ValueError:
        print("Invalid Input!")
        quit() 
    try:
        Max_iter=int(arglist[2])
    except ValueError:
        print("Invalid Input!")
        quit() 

    if (checktype(arglist[1]) or int(arglist[1])<2):
        print("Invalid Input!")
        sys.exit(1)
    if (checktype(arglist[2]) or int(arglist[2])<1):
        print("Invalid Input!")
        sys.exit(1)
    try:
        eps=float(arglist[3])
    except ValueError:
        print("Invalid Input!")
        quit() 

    In_filename1=arglist[4]
    In_filename2=arglist[5]

elif len(sys.argv)==5:
    try:
        K=int(arglist[1])
    except ValueError:
        print("Invalid Input!")
        quit() 

    if (checktype(arglist[1]) or int(arglist[1])<2):
        print("Invalid Input7!")
        sys.exit(1)
    
    try:
        eps=float(arglist[2])
    except ValueError:
        print("Invalid Input!")
        quit()
    
    In_filename1=arglist[3]
    In_filename2=arglist[4]

if 'Max_iter' not in locals():
    Max_iter=200


#data
input1=pd.read_csv(In_filename1,delimiter=',',header=None)
input2=pd.read_csv(In_filename2,delimiter=',',header=None)
inner=pd.DataFrame.merge(input1,input2,how='inner',left_on=0,right_on=0)
inner.set_index(inner[0],inplace=True)
inner=inner.iloc[:,1:]
N=inner.shape[0]


def find_argmin_cluster_to_point(centroid_list,point,i): 
    min=sys.maxsize
    for j in range(i):
        sub=np.subtract(point,centroid_list[j])
        temp=np.dot(sub,sub)
        if temp<min:
            min=temp
    return min

i=1
centroid_list=[None]*K
D=[0]*N
P=[0]*N
centorid1=inner.loc[np.random.choice(N)]
centroid_list[0]=centorid1
while i<K:
    for l in range(N):
        D[l]=find_argmin_cluster_to_point(centroid_list,inner.loc[l],i)
    for l in range(N):
        P[l]=D[l]/np.sum(D)
    i+=1
    centroid_list[i-1]=inner.loc[np.random.choice(N,p=P)]
result_index=[]
res_centroids=[]
for centroid in centroid_list:
    res_centroids.append(centroid.to_numpy())
    result_index.append(int(centroid.name))




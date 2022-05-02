import numpy as np
from numpy import genfromtxt
import pandas as pd
import sys
np.random.seed(0)

#input
input1=pd.read_csv('input_1_db_1.txt',delimiter=',',header=None)
input2=pd.read_csv('input_1_db_2.txt',delimiter=',',header=None)
inner=pd.DataFrame.merge(input1,input2,how='inner',left_on=0,right_on=0)
inner=inner.iloc[:,1:]
inner_array=inner.to_numpy() 
N=inner_array.shape[0]
K=3

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
centorid1=inner_array[np.random.choice(N)]
centroid_list[0]=centorid1
while i<K:
    for l in range(N):
        D[l]=find_argmin_cluster_to_point(centroid_list,inner_array[l],i)
    for l in range(N):
        P[l]=D[l]/np.sum(D)
    i+=1
    centroid_list[i-1]=inner_array[np.random.choice(N,p=P)]
for centroid in centroid_list:
    index=np.where(inner_array==centroid)
    print(index[0][0])


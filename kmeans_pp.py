import numpy as np
from numpy import genfromtxt
import pandas as pd
np.random.seed(0)

input1=pd.read_csv('input_1_db_1.txt',delimiter=',',header=None)
input2=pd.read_csv('input_1_db_2.txt',delimiter=',',header=None)
inner=pd.merge(input1,input2,left_on=0,right_on=0)
inner_array=inner.to_numpy() 
print(inner_array)
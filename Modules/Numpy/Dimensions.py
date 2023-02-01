import numpy as np 

drr = np.array([1,2,3,4])      #1 Dimension array
print(drr.ndim)

drr1 = np.array([[1,2,3],[4,5,6]])      #2 Dimension array
print(drr1.ndim)

drr2 = np.array([[[1,2,3,4], [5,6,7,8], [12,34,12,23]]])       #3 Dimension array
print(drr2.ndim)
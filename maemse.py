import numpy as np
X = np.array([[-1, 1], [4, 1], [4, 1], [8, 1], [10, 1]]) 
y = np.array([0, 4, 6, 8, 12])
w = np.array([1, 0.85])
result=y-X@w
print("Residuals:",result)
mae=abs(result).mean()
mse=(abs(result)**2).mean()
print("L1 or mean absolute error:",mae)
print("L2 or mean squared error:", mse)
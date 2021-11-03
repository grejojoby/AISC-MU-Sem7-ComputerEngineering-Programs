import numpy as np

def linear_threshold_gate(dot: int, T: float) -> int:
    if dot >= T:
        return 1
    else:
        return 0

input_table = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1] 
])

print('\nAND gate')
print("+---------------+----------------+")
print(" | AND Truth Table | Result |")
print(" X1 | X2 | AND")
print(" 0  | 0  |  0| ")
print(" 0  | 1  |  0| ")
print(" 1  | 0  |  0| ")
print(" 1  | 1  |  1| ")
weights = np.array([1,1])
print("Assuming Weights w1=1 and w2=1")
dot_products = input_table @ weights
print("yin=w1.x1+ w2.x2")
print(f'Yin result: {dot_products}')
T = 2
for i in range(0,4):
    activation = linear_threshold_gate(dot_products[i], T)
res=(2*1-0)
print("Threshold value(theta):",T)
print("theta>=nw-p")
print("theta >= 2*1-0")
if(T >= res ):
    print("neurons fired")
else:
    print("neurons not fired")

print('\nOR gate')
print("+---------------+----------------+")
print(" | OR Truth Table | Result |")
print(" X1 | X2 | OR")
print(" 0  | 0  |  0| ")
print(" 0  | 1  |  1| ")
print(" 1  | 0  |  1| ")
print(" 1  | 1  |  1| ")
weights = np.array([1,1])
print("Assuming Weights w1=1 and w2=1")
print("yin=w1.x1+ w2.x2")
dot_products = input_table @ weights
print(f'Yin Result: {dot_products}')
T1 = 1
for i in range(0,4):
    activation = linear_threshold_gate(dot_products[i], T1)
res1=(1*1-0)
print("Threshold value(theta):",T1)
print("theta>=nw-p")
print("theta >= 1*1-0")
if(T1 >= res1 ):
    print("neurons fired")
else:
    print("neurons not fired")

print('\nNOT gate')
print("+---------------+----------------+")
print(" | NOT Truth Table | Result |")
print(" X1 | X2 | NOT")
print(" 0  | 0  |  1| ")
print(" 0  | 1  |  0| ")
print(" 1  | 0  |  0| ")
print(" 1  | 1  |  0| ")
weights = np.array([-1,-1])
print("Assuming Weights w1=-1 and w2=-1")
dot_products = input_table @ weights
print("yin=w1.x1+ w2.x2")
print(f'Yin Result: {dot_products}')
T2 = 0
for i in range(0,4):
    activation = linear_threshold_gate(dot_products[i], T2)
res2=(0*1-0)
print("Threshold value(theta):",T2)
print("theta>=nw-p")
print("theta >= 0*(-1)-0")
if(T2 >= res2 ):
    print("neurons fired")
else:
    print("neurons not fired")
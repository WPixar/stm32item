import numpy as np

import time
t1 = time.time()
l = list(range(100))
for _ in range(10000):
    l = list(map(lambda i: i + 1, l))
print(l)
print("时间为{:.4f}s".format(time.time() - t1))

import numpy as np
cars11 =np.array([12,3,4,4])
cars12 =np.array([12,3,4,4])
test1=np.expand_dims(cars11,0)
test2=np.expand_dims(cars11,1)
# test3=np.expand_dims(cars11,2)
print(test1)
print(test2)



print(np.concatenate([cars11,cars12]))
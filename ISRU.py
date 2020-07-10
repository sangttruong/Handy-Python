import math
def ISRU(x):
  a = 1
  return x / (math.sqrt(a + x**2))

y = []
x = []
import numpy as np
for i in np.arange(0,8,0.5):
  x.append(i)
  y.append(ISRU(i))

import matplotlib.pyplot as plt
plt.figure(figsize = (10,5))
plt.plot(x, y)
plt.show()

ISRU(0.23)

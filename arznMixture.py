import matplotlib.pyplot as plt
import numpy as np
import plotly.express as alpha
import plotly
import array as arr
c=9
a = 0.1*np.ones((c,c))
a[0][0]=0.5
b = np.arange(c,0,-1)
i=0
j=0
# Solid zinc is surrounded by argon and the metal is dissolved by a mixed process gas
# creating array
k = arr.array('i', [1, 2, 3])
# iterating and printing each item
#for i in range(0, 3):
#    print(k[i], end=" ")
for z in range(1,6,1):
  for y in range(7,2,-1):
    i=int(y)
    j=int(z)
    a[j][i]=0.9
fig = alpha.imshow(a,text_auto=True)
fig.show()
#plotly.offline.plot(fig, filename='alpha.html')

import matplotlib.pyplot as plt
import numpy as np
import plotly.express as alpha
import plotly
import array as arr
c=10
a = 0.1*np.ones((c,c))
beam = np.ones((c,c))
a[0][0]=0.5
b = np.arange(c,0,-1)
i=0
j=0
# Solid zinc is surrounded by argon and the metal is dissolved by a vof laser
# creating array
k = arr.array('i', [1, 2, 3])
# iterating and printing each item
for z in range(1,c-3,1):
  for y in range(c-3,1,-1):
    i=int(y)
    j=int(z)
    a[j][i]=0.9
i=0
j=0
for z in range(int(c/2),-int(c/2),-1):
  for y in range(-int(c/2),int(c/2),1):
    i=int(y)
    j=int(z)
    beam[j][i]=((i+j)/c)**2
rayf=a*beam;
fig = alpha.imshow(rayf,text_auto=True)
fig.show()
#plotly.offline.plot(fig, filename='alpha.html')

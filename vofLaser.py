import matplotlib.pyplot as plt
import numpy as np
import numpy
import plotly.express as alpha
import plotly
import array as arr
c=20
a = 0.1*np.ones((c,c))
beam = np.ones((c,c))
a[0][0]=0.5
b = np.arange(c,0,-1)
i=0
j=0
for z in range(int(c/2),-int(c/2),-1):
  for y in range(-int(c/2),int(c/2),1):
    i=int(y)
    j=int(z)
    r=numpy.sqrt(i**2+j**2)
    beam[j][i]=numpy.exp(-r**2/c**2)
    beam[j][i]=beam[j][i]/beam.max()
rayf=a*beam;
#beam=100*beam;
# Solid zinc is surrounded by argon and molten 
# by a laser beam via creating an array
i=0
j=0
# iterating and printing each item
for z in range(1,int(c/2)+1,1):
  for y in range(int(c)-2,int(c/2)-2,-1):
    i=int(y)
    j=int(z)
    #beam[j][i]=0
fig = alpha.imshow(beam,text_auto=True)
fig.show()
#plotly.offline.plot(fig, filename='alpha.html')

"""
     三角信号
"""
import numpy as np
import matplotlib.pyplot as plt

def triangle_wave(x,c,hc):    #幅度为hc，宽度为c,斜度为hc/2c的三角波
     if x>=c/2:
          r = 0.0
     elif x<=-c/2:
          r = 0.0
     elif x > -c/2 and x<0:
          r=2*x/c*hc+hc
     else:
          r=-2*x/c*hc+hc
     return r

x=np.linspace(-3,3,1000)
y=np.array([triangle_wave(t,4.0,1.0) for t in x])
plt.ylim(-0.2,1.2)
plt.plot(x,y)
plt.show()
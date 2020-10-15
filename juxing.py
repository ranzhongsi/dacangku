"""
     矩形脉冲信号
"""

import numpy as np
import matplotlib.pyplot as plt

def rect_wave(x,c,c0):     #起点为c0，宽度为c的矩形波
     if x>=(c+c0):
          r=0.0
     elif x<c0:
          r=0.0
     else:
          r=1
     return r

x=np.linspace(-2,4,1000)
y=np.array([rect_wave(t,2.0,-1.0) for t in x])
plt.ylim(-0.2,1.2)
plt.plot(x,y)
plt.show()

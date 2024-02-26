
# coding: utf-8

# In[2]:

import pandas
import numpy as np
from scipy.fftpack import fft, ifft
import matplotlib.pyplot as plt

data = "D:\\python_code\\fft\siganl_sin.csv"
names = ['number','x_signal','y_signal']
dataset = pandas.read_csv(data, names=names)
#dataset = pandas.read_csv(data)
#print dataset
array = dataset.values
x1= array[:,1]
y1= array[:,2]
plt.plot(x1, y1)
plt.grid()
plt.show()
#print y
N = 600
T = 1.0 / 800
yf1 = fft(y1)
#print len(yf1[0:N//2])
xf1 = np.linspace(0.0, 1.0/(2.0*T), N//2)
#xf1 = range(0,300)
#print xf1
import matplotlib.pyplot as plt
plt.plot(xf1, np.abs(yf1[0:N//2]))
plt.grid()
plt.show()

yinv = ifft(yf1)
plt.plot(x1,yinv)
plt.grid()
plt.show()






# In[ ]:




# In[ ]:




# In[ ]:




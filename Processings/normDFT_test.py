import numpy as np
import matplotlib.pylab as plt
from normDFT import normDFT
secs = 1
N = 1000 # number of samples/sec
n = np.linspace(0,secs-(1/N), secs*N)
#print(n)
x = np.cos(2*np.pi*117*n)
[nf,xf] = normDFT(x,secs*N)
[nfb,xfb] = normDFT(x*np.blackman(N),secs*N)
plt.figure(1)
plt.plot(nf,xf)
plt.figure(2)
plt.plot(nfb,xfb)
plt.show()

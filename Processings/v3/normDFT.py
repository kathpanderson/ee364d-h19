# plot of normalized fourier of data with hight normalized by:
# 1. points in DFT
# 2. maximum frequency component as logrithmic refrence
# 3. normalized frequency by sampling rate
# 4. only include half the DFT that has the amplitude information
#inputs: time domain data
#outputs: normalized DFT of input and normalized frequency as well
import numpy as np

def normDFT(xn,N):
    nf = np.arange(0,0.5,(1/N))
    Xf = np.abs(np.fft.fft(xn))/(N/2)
    M = np.amax(Xf)
    normXf = 20*np.log10(Xf[0:int(N/2)]/M)
    return [nf,normXf]
    #plot(nf,normXf)
    #title('Normalized DFT')

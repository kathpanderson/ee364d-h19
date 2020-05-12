# plot of normalized fourier of data with hight normalized by:
# 1. points in DFT
# 2. maximum frequency component as logrithmic refrence
# 3. normalized frequency by sampling rate
# 4. only include half the DFT that has the amplitude information
#inputs: time domain data
#outputs: normalized DFT of input and normalized frequency as well
import numpy as np
import matplotlib.pyplot as plt

def normDFT(xn,N):
    #nf = np.arange(0,0.5,(1/N))
    Xf = np.abs(np.fft.fft(xn))/(N/2)
    M = np.amax(Xf)
    normXf = [-300 if i == 0.0 else 20*np.log10(i/M) for i in Xf]
    #if M !=0:
    #	normXf = 20*np.log10(Xf[0:int(N/2)]/M)
    return normXf[0:int(N/2)] #[nf,normXf]

def main():
	N = 1000
	n = np.linspace(0, 1-1/N, N)
	xn = np.sin(2*np.pi*10*n)
	normXf = normDFT(xn, len(xn))
	plt.figure(1)
	plt.plot(n, xn)
	plt.figure(2)
	plt.plot(normXf)
	plt.show()

if __name__ == '__main__':
    main()
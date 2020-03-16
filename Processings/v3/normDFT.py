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
	nf = np.arange(0,0.5,(1/N))
	Xf = np.abs(np.fft.fft(xn))/(N/2)
	M = np.amax(Xf)
	normXf = 20*np.log10(Xf[0:int(N/2)]/M)
	return [nf,normXf]

def main():
	fs = 4000000.0 #samples/seconds
	fsin = 1000000
	time = 1 #seconds
	t = np.linspace(0, time, time*fs, endpoint = False)
	y = np.sin(2*np.pi*fsin*t)
	N = time*fs #float(len(y))
	print("N IS HERE:", N)
	DFT = normDFT(y,N)
	plt.plot(DFT[0],DFT[1])
	plt.title('Normalized DFT')
	plt.show()

if __name__ == '__main__':
	main()
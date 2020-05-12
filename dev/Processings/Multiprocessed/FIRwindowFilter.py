import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig

def FIRwindowFilter(signal,sample_rate,cutoff_hz):
	# Design filter
	N = 200 #number of coefficients
	nyq_rate = sample_rate/2
	b = sig.firwin(N,cutoff_hz/nyq_rate) #0.5 times Nyquist
	filtered = np.convolve(signal, b,'same')
	return filtered

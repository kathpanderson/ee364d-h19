# determining threshold value of each frequency signal and zeroing out all values below threshold
# sent in n_spm
# passed to us
# needs to iterate through x, y and thr frequency
# libraries to get: numpy & matlibplot & movie
# np.max()
import numpy as np
import math
from numpy.random import rand
# function: threshold
# inputs: n_spm (noise power of spm) and snr_spm (snr of spm) and array of form data[x][y][f]
# outputs: data threshold-ed
# function definition: to find the threshold value of the signal
def thresholder(n_spm_dB, snr_spm_dB, noiseRejection, data):
    print("Start thresholder")
    # Create output structure
    output_data = []
    for freq in range(0,len(data[0][0])):
        output_data.append([])
    #Calculations for threshold
    n_spm = pow(10,n_spm_dB/10) # convert to linear before minipulation
    snr_spm = pow(10,snr_spm_dB/10) # convert to linear before minipulation
    noise = pow(noiseRejection, 2)*n_spm
    b = 16                                  # number of bits
    lsb = 20/(pow(2, b))    # least significant bit = Vpp/2^b (assume Vpp is 20)
    qn = pow(lsb, 2)/12 # quantized noise from the DAQ
    p_sig = n_spm*snr_spm   # snr = signal power/noise power
    snr_tot = p_sig / (noise + qn)  # total SNR calc (assumes that gain is v big so snr_spm ~= snr_amp)
    thrNoise = -10*math.log(snr_tot, (10)) # threshold for normalized data without spreading in frequency
    thr = thrNoise-10*math.log(len(data[0][0]), (10)) # threshold for normalized data
    print("Threshhold value:", thr,"\n")
    # threshold data and restore 
    for freq in range(0, len(data[0][0])):
        for i in range(0, len(data)):
            for j in range(0, len(data[0])):
                if data[i][j][freq] > thr:
                    output_data[freq].append([i, j, data[i][j][freq]]) #reorgonize as [f][point](x,y,valueF)
    return output_data

def main():
    dimensions = 3
    data = make_array(dimensions)
    n_spm = 1 #dB
    spm_snr = 10 #dB
    noiseRejection = 1# number of noise standard deviations 
    output_data = thresholder(n_spm, spm_snr, noiseRejection, data)
    print("OUTPUT DATA")
    for i in range(len(output_data)):
        print("Frequency: ", i)
        for j in range(len(output_data[i])):
            print(output_data[i][j])

# import data in as a function
def make_array(dimensions):
    arr = np.zeros((dimensions, dimensions, dimensions))
    for l in range(dimensions):
        for m in range(dimensions):
            for n in range(dimensions):
                arr[l][m][n] = 20*math.log(rand(),10)
    print("INPUT DATA")
    print(arr,"\n")
    return arr

if __name__ == '__main__':
    main()
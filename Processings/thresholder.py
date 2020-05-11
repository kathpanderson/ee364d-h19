# determining threshold value of each frequency signal and zeroing out all values below threshold
# sent in n_spm
# passed to us
# needs to iterate through x, y and thr frequency
# libraries to get: numpy & matlibplot & movie
# np.max()


import numpy as np
import pywt
import math
from numpy.random import seed
from numpy.random import rand
seed(1)


def main():
#    data = make_array()
    output_data = thresholder(n_spm, spm_snr, data)
    return output_data


# import data in as a function
def make_array():
    i = j = k = 3
    l = m = n = 0
    arr = np.zeros((i, j, k))
    for l in range(i):
        for m in range(j):
            for n in range(k):
                arr[l][m][n] = rand()
    print(arr)
    return arr


# function: threshold data
# function description: zero out all values at and below the threshold
# input: threshold value
# output: nothing? change the value in the data set
def threshold_data(thr, data):
    data = pywt.threshold(data, thr, mode='hard', substitute=0)
    return data


# function: threshold
# inputs: n_spm (noise power of spm) and snr_spm (snr of spm) and array of form data[x][y][f]
# outputs: data threshold-ed
# function definition: to find the threshold value of the signal
def thresholder(n_spm, snr_spm, data):
    b = 16						                    # number of bits
    i = 0
    j = 0
    k = 0
    boop = len(data)*len(data[0])
    bop = len(data[0][0])
    output_data = np.zeros((bop, boop, 3))
    print(output_data)
    p_sig = n_spm * snr_spm				            # snr = signal power/noise power
    lsb = 20/(pow(2, b))				            # least significant bit = Vpp/2^b (assume Vpp is 20)
    qn = pow(lsb, 2)/12				                # quantized noise from the DAQ
    adj_qn = qn - (len(data)/2)		                # adjusted noise threshold level - shift down by (size(array)/2)
    snr_tot = p_sig / (n_spm + adj_qn)	            # total SNR calc (assumes that gain is v big so snr_spm ~= snr_amp)
    n = len(data)
    print(n)
    # threshold up here
    thr = -10*math.log(snr_tot, (10))
    # signal max is 0db -- subtracting logs
    doo = 0

    for i in range(0, n):
        for j in range(0, len(data[0])):
            print(data[i][j])
            data[i][j] = threshold_data(thr, data[i][j])
            for k in range(0, len(data[0][0])):
                output_data[k][doo] = [i, j, data[i][j][k]]
            doo = doo + 1
    return output_data


if __name__ == '__main__':
    main()


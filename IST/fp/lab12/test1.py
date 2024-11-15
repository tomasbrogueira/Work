#create a fast fourier transform of a signal without using numpy

import math
from math import sin, exp, pi, ceil, log2

# create a signal
t = [i/1000 for i in range(1000)]
x = [sin(2*pi*50*t[i]) + 0.5*sin(2*pi*120*t[i]) for i in range(1000)]
# compute the FFT
def fft(x):
    # pad the signal with zeros
    x = x + [0] * (2**ceil(log2(len(x))) - len(x))
    # split the signal into even and odd parts
    even = x[::2]
    odd = x[1::2]
    print("Even:", even)
    print("Odd:", odd)
    # compute the FFT of the even part
    even = fft(even)
    # compute the FFT of the odd part
    odd = fft(odd)
    print("Even:", even)
    print("Odd:", odd)
    print("Even + odd:", even + odd)
    # compute the FFT of the signal
    X = [0] * len(x)
    for i in range(len(x)//2):
        X[i] = even[i] + exp(-2j*pi*i/len(x)) * odd[i]
        X[i+len(x)//2] = even[i] - exp(-2j*pi*i/len(x)) * odd[i]
    return X
#create a fast fourier transform of a signal without using numpy

import math
from math import sin, exp, pi, ceil, log2

# create a signal
t = [i/1000 for i in range(1000)]
x = [sin(2*pi*50*t[i]) + 0.5*sin(2*pi*120*t[i]) for i in range(1000)]
# compute the FFT
def fft(x):
    # pad the signal with zeros
    x = x + [0] * (2**ceil(log2(len(x))) - len(x))
    # split the signal into even and odd parts
    even = x[::2]
    odd = x[1::2]
    # compute the FFT of the even part
    print("even: ", even)
    even = fft(even)
    print("even: ", even)
    # compute the FFT of the odd part
    print("odd: ", odd)
    odd = fft(odd)
    print("odd: ", odd)
    # compute the FFT of the signal
    X = [0] * len(x)
    for i in range(len(x)//2):
        X[i] = even[i] + exp(-2j*pi*i/len(x)) * odd[i]
        X[i+len(x)//2] = even[i] - exp(-2j*pi*i/len(x)) * odd[i]
    return X

X = fft(x)

# compute the frequencies
freqs = [i*1000/len(x) for i in range(len(x))]
# plot the signal
plt.figure()

X = fft(x)

# compute the frequencies
freqs = [i*1000/len(x) for i in range(len(x))]
# plot the signal
plt.figure()
plt.plot(t, x)
plt.xlabel('Time [s]')
plt.ylabel('Signal amplitude')

# plot the FFT magnitude
plt.figure()
plt.stem(freqs, abs(X))
plt.xlabel('Frequency in Hertz [Hz]')
plt.ylabel('Frequency Domain (Spectrum) Magnitude')
plt.xlim(-100, 100)
plt.show()

# Path: fp\lab12\test1.py

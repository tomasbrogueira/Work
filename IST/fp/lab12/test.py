#create a fast fourier transform of a signal
import numpy as np
import matplotlib.pyplot as plt

# create a signal
t = np.linspace(0, 1, 1000)
x = np.sin(2*np.pi*50*t) + 0.5*np.sin(2*np.pi*120*t)

# compute the FFT
X = np.fft.fft(x)

# compute the frequencies
freqs = np.fft.fftfreq(len(x)) * 1000

# plot the signal
plt.figure()
plt.plot(t, x)
plt.xlabel('Time [s]')
plt.ylabel('Signal amplitude')

# plot the FFT magnitude
plt.figure()
plt.stem(freqs, np.abs(X))
plt.xlabel('Frequency in Hertz [Hz]')
plt.ylabel('Frequency Domain (Spectrum) Magnitude')
plt.xlim(-100, 100)
plt.show()

# Path: fp\lab12\test.py
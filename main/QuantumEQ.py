import math
import numpy as np
import librosa
from IPython.display import Audio
from librosa import display
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister
# from qiskit import assemble, Aer, execute
from qiskit import transpile # replaces assemble
# from qiskit_ibm_runtime import QiskitRuntimeService, Session, Options # replaces execute
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from sympy import *

musicbar = 'A-strich'
file_path = './sound_samples/'+str(musicbar)+'.wav'

# sr = sample rate, original value = 44100
samples, sampling_rate= librosa.load(file_path, sr = None, mono = True, offset= 0.0, duration = None) 
samples = samples.astype('float64')
print("length of the sample:",len(samples)/sampling_rate,"seconds")
print("sampling rate:",sampling_rate,"Hz")
print("Number of samples:",samples.size)

#plot the first 500 smaple points to get a sense of the data

n=500

x = np.arange(n)
x = x/sampling_rate*1000
y = samples[0:n]
plt.title(musicbar) 
plt.xlabel("time in ms") 
plt.ylabel("amplitude") 
plt.plot(x,y,"o") 
plt.plot(x,y)
plt.show()
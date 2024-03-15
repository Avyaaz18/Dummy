import numpy as np
from scipy import signal

# Define the transfer function
num = [14.4]
den = [0.1, 1, 14.4]
sys = signal.TransferFunction(num, den)

# Create a frequency range
w = np.logspace(-1, 2, 1000)

# Calculate the magnitude and phase of the transfer function
w, mag, phase = signal.bode(sys, w)

# Save the data to .txt files
np.savetxt('magnitude_data.txt', np.column_stack((w, mag)), delimiter=',', header='Frequency,Magnitude', comments='')
np.savetxt('phase_data.txt', np.column_stack((w, phase)), delimiter=',', header='Frequency,Phase', comments='')
import numpy as np
from scipy import signal

# Define the transfer function
num = [14.4]
den = [0.1, 1, 14.4]
sys = signal.TransferFunction(num, den)

# Create a frequency range
w = np.logspace(-1, 2, 1000)

# Calculate the magnitude and phase of the transfer function
w, mag, phase = signal.bode(sys, w)

# Save the data to .txt files
np.savetxt('magnitude_data.txt', np.column_stack((w, mag)), delimiter=',', header='Frequency,Magnitude', comments='')
np.savetxt('phase_data.txt', np.column_stack((w, phase)), delimiter=',', header='Frequency,Phase', comments='')

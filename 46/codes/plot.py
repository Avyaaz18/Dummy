import numpy as np
import matplotlib.pyplot as plt

# Load data from magnitude_data.txt and phase_data.txt
mag_data = np.loadtxt('magnitude_data.txt', delimiter=',', skiprows=1)
phase_data = np.loadtxt('phase_data.txt', delimiter=',', skiprows=1)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

# Plot magnitude in the first subplot
ax1.semilogx(mag_data[:, 0], mag_data[:, 1])
ax1.set_ylabel(r'$20\log{|T|}$')
ax1.grid(True)

# Plot phase in the second subplot
ax2.semilogx(phase_data[:, 0], phase_data[:, 1])
ax2.set_xlabel(r'$\omega$')
ax2.set_ylabel('Phase [degrees]')
ax2.grid(True)

# Adjust layout and save the plot
plt.tight_layout()
plt.savefig('plot.png')
plt.show()

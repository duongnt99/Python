import numpy as np
import math
import matplotlib.pyplot as plt


frequency = 60
T = 1/60
Nt = 5
Ns = 1000

t = np.arange(0, Nt*T, Nt*T/Ns)
sin_t = np.sin(2*math.pi*frequency*t)
fig = plt.figure()


print(t)
print(sin_t)
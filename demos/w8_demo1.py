import matplotlib.pyplot as plt
from matplotlib.ticker import Multiplelocator

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

#fig, ax = plt.subplots(3, 2)
fig = plt.figure()

ax1 = fig.add_subplot(3, 2, 3)
ax2 = fig.add_subplot(3, 2, 6)
ax1.set_xlabel("Random data X")
ax2.set_ylabel("No ideea what's here")
ax1.set_xlim(1,3)



ax1.plot(x,y, "rx")
ax2.plot(x,y, "bo")

plt.show()
from pylab import *

# get current axis
ax = gca()

# set view to tight, and maximum number of tick intervals to 10
ax.locator_params(tight=True, nbins=20)

# generate 100 normal distribution values
ax.plot(np.random.normal(20, .5, 200))

show()

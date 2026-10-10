import pylab
import numpy as np

# Create x values
x = np.linspace(-5, 5, 100)

# Calculate y values
y = x ** 2

# Plot the curve
pylab.plot(x, y)

# Add title and labels
pylab.title("Plotting a Curve")
pylab.xlabel("X Values")
pylab.ylabel("Y Values")

# Display the graph
pylab.show()
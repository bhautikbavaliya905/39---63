import pylab

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# 1. Line Plot
pylab.figure()
pylab.plot(x, y)
pylab.title("Line Plot")
pylab.xlabel("X Values")
pylab.ylabel("Y Values")
pylab.show()

# 2. Bar Chart
pylab.figure()
pylab.bar(x, y)
pylab.title("Bar Chart")
pylab.xlabel("X Values")
pylab.ylabel("Y Values")
pylab.show()

# 3. Pie Chart
pylab.figure()
data = [30, 20, 25, 25]
labels = ["A", "B", "C", "D"]
pylab.pie(data, labels=labels, autopct="%1.1f%%")
pylab.title("Pie Chart")
pylab.show()

# 4. Histogram
pylab.figure()
marks = [45, 50, 55, 60, 65, 65, 70, 75, 75, 80, 85, 90]
pylab.hist(marks, bins=5)
pylab.title("Histogram")
pylab.xlabel("Marks")
pylab.ylabel("Frequency")
pylab.show()

# 5. Scatter Plot
pylab.figure()
pylab.scatter(x, y)
pylab.title("Scatter Plot")
pylab.xlabel("X Values")
pylab.ylabel("Y Values")
pylab.show()
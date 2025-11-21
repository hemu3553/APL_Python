# ------------------------------------------------------------------------------------------------------------
#  * Python Programming for Data Scientists and Engineers
#  * ICE #6 Linear Regression with numpy + matplotlib
#  * #11 Chia-Hui Amy Lin
# ------------------------------------------------------------------------------------------------------------
# Libraries
import numpy as np
import matplotlib.pyplot as plt
from pylab import figtext
from sklearn import linear_model

# x, y data points
x_axis = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y_axis = [1, 3, 2, 5, 7, 8, 8, 9, 10, 12]

# Reshape the x and y numpy array
x_axis = np.reshape(x_axis, (len(x_axis), 1))
y_axis = np.reshape(y_axis, (len(y_axis), 1))

# Build a LR model
LR_Model = linear_model.LinearRegression()

# Throw the data points into the model
LR_Model.fit(x_axis, y_axis)

# Calculate the coefficient of the LR model
coefficient = LR_Model.coef_

# Plot the data points on the graph
plt.scatter(x_axis, y_axis, color='red')

# Plot the Linear Regression Line
plt.plot(x_axis, LR_Model.predict(x_axis), color='blue', linewidth=3)

# Title for the graph
plt.suptitle("Linear Regression", fontsize=30)
# X legend
plt.xlabel("x-axis", fontsize=20)
# Y legend
plt.ylabel("y-axis",  fontsize=20)

# Sub texts at the bottom of the graph
plt.subplots_adjust(bottom=0.25)
figtext(.1, .09, "* Coefficient :" + str(coefficient), fontsize=16)

# Output the graph
plt.show()


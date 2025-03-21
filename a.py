import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg

# Load an image
img = mpimg.imread("your_image.png")

# Create figure and axis
fig, ax = plt.subplots()

# Display image
ax.imshow(img)

# Define points (x, y)
points = np.array([[100, 150], [200, 300], [400, 100]])
labels = ["Point A", "Point B", "Point C"]

# Plot points
ax.scatter(points[:, 0], points[:, 1], color='red', s=100)

# Annotate points
for i, (x, y) in enumerate(points):
    ax.annotate(labels[i], (x, y), textcoords="offset points", xytext=(10,10), ha='right',
                arrowprops=dict(arrowstyle="->", color='blue'))

# Show plot
plt.show()

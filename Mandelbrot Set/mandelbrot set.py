import numpy as np
import matplotlib.pyplot as plt

# Define a function to check if a complex number belongs to the Mandelbrot set
def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2.0:
            return n
        z = z * z + c
    return max_iter

# Define the parameters for the Mandelbrot set
width, height = 800, 800
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5
max_iter = 256

# Create an empty image to store the Mandelbrot set
mandelbrot_image = np.zeros((height, width))

# Generate the Mandelbrot set
for x in range(width):
    for y in range(height):
        real = x_min + (x / (width - 1)) * (x_max - x_min)
        imag = y_min + (y / (height - 1)) * (y_max - y_min)
        c = complex(real, imag)
        mandelbrot_image[y, x] = mandelbrot(c, max_iter)

# Plot the Mandelbrot set
plt.imshow(mandelbrot_image, extent=(x_min, x_max, y_min, y_max))
plt.show()
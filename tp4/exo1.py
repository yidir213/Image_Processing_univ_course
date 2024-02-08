from PIL import Image, ImageFilter, ImageChops
import numpy as np

# 1. Read an image in color
image = Image.open("../F.jpg")

# 2. Display the image
image.show()

# 3. Print the format, dimensions, and representation mode of the image
width, height = image.size
print(f"Dimensions: {width}x{height}")
print(f"Mode: {image.mode}")

# 4. Display the red, green, and blue channels
r, g, b = image.split()
r.show("Red Channel")
g.show("Green Channel")
b.show("Blue Channel")

# 5. Convert image to grayscale
img_gris = image.convert("L")
img_gris.show("Grayscale Image")

# 6. Find the inverse image
img_inverse = ImageChops.invert(img_gris)
img_inverse.show("Inverse Image")

# 7. Save the inverse image
img_inverse.save('ImgInverse.jpg')

# 8. Filter the images using the mentioned filters

# Mean filter
img_mean = img_gris.filter(ImageFilter.BoxBlur(5))
img_mean.show("Mean Filter")

# Median filter
img_median = img_gris.filter(ImageFilter.MedianFilter(5))
img_median.show("Median Filter")

# Maximum filter
# For Maximum filter with Pillow, we need to use ImageFilter.MaxFilter
img_maximum = img_gris.filter(ImageFilter.MaxFilter(5))
img_maximum.show("Maximum Filter")

# Minimum filter
# For Minimum filter with Pillow, we need to use ImageFilter.MinFilter
img_minimum = img_gris.filter(ImageFilter.MinFilter(5))
img_minimum.show("Minimum Filter")





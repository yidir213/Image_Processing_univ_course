# Exercice 2 :
# Ecrire un script python qui affiche l’image A avec seulement deux couleurs : le noir et le blanc.

from PIL import Image
import numpy as np

# Load the image
image = Image.open("Tp1/A.jpg")

# Convert the image to grayscale
img_gris = image.convert("L")

# Threshold the image to get a binary image (black and white)
threshold = 128  # This is a standard value. Adjust as needed.
img_gris=np.array(img_gris)
binary_image=np.empty_like(img_gris)
row, column= binary_image.shape
for x in range(row):
    for y in range(column):
        binary_image[x,y] = 0 if img_gris[x,y] <= threshold else 255
        
# Display the binary image
Image.fromarray(binary_image).show()




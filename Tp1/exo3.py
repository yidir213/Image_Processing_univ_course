# Exercice 3 :
# Téléchargez les images suivantes : B.jpg, C.jpg, D.jpg.
# En utilisant le langage de programmation Python, écrire un script python qui permet de :
# 1) Accéder à un pixel donné dans l’image B,
# 2) Modifier un pixel donné dans l’image B,
# 3) Calculer la luminosité pour chaque pixel de l’image B, sachant que l= (r+g+b)/3,
# 4) Convertir l’image B (RGB) vers une image en niveau de gris,
# 5) Extraire le canal rouge, vert et bleu de l’image D,
# 6) Calculer le négatif (complément d’un pixel) de l’image D.


from PIL import Image
import numpy as np

# Load the image B et Convertir en array
img_b = Image.open("Tp1/B.jpg")
img_b=np.array(img_b)

# 1) Access a given pixel in image B
x, y = 50, 50  # coordinates of the pixel to access
pixel_value = img_b[x,y]
print(f"Pixel value at ({x}, {y}): {pixel_value}")

# 2) Modify a given pixel in image B
new_value = (255, 0, 0)  # for example, change to red
img_b[x, y]= new_value

# 3) Calculate brightness for each pixel in image B
width, height, _ = img_b.shape
for i in range(width):
    for j in range(height):
        r, g, b = img_b[i, j]
        l = (r + g + b) / 3

# 4) Convert image B (RGB) to grayscale
l = []
for row in img_b:
    ligne = []
    for pix in row:
        ligne.append(sum(pix)/3) # row est un tableau de 3 valeur (R,G, B)
    l.append(ligne)
#or 
l1 = [[(sum(pix) / 3) for pix in row] for row in img_b ]

# 5) Extract the red, green, and blue channels from image D

red, blue, green = [], [], []
for row in img_b:
    row_red, row_blue, row_green = [], [], []
    for pix in row :
        row_red.append([pix[0], 0, 0])
        row_green.append([0, pix[1], 0])
        row_blue.append([0, 0, pix[2]])
        
    red.append(row_red)
    blue.append(row_blue)
    green.append(row_green)

# Show red channel of image
    
red = np.array(red, dtype=np.uint8)
Image.fromarray(red).show()

# or 
red = [  [[pix[0], 0, 0] for pix in row]  for row in img_b] # pour chaque row in img, nous avons un tableau [[pix[0], 0, 0] for pix in row]

# Show green channel of image
    
green = np.array(green, dtype=np.uint8)
Image.fromarray(green).show()

# Show green channel of image

blue = np.array(blue, dtype=np.uint8)
Image.fromarray(blue).show()

# essayer de faire la question 6, le négatif de l’image D.

# 6) Calculate the negative of image D
img_b_negative=np.empty_like(img_b)
for i in range(width):
    for j in range(height):
        r, g, b = img_b[i, j]
        img_b_negative[i, j] = (255 - r, 255 - g, 255 - b)

Image.fromarray(img_b_negative).show()




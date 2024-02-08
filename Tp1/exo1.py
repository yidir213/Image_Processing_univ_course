

# Exercice 1 :
# Téléchargez l'image suivante : A.jpg
# Ecrire un script python en utilisant la bibliothèque PIL pour :
# 1) Afficher la taille et le format de l'image,
# 2) Afficher la valeur du pixel de coordonnée (400,250),
# 3) Modifier sa valeur pour qu'elle soit égale à (250, 250, 250),
# 4) Enregistrer l'image sous le nom de « M.jpg »
# 5) Afficher l'image avec Python.

from PIL import Image
import numpy as np


# 1) Ouvrir l'image
img_a = Image.open("Tp1/A.jpg")

# 2) Afficher la taille et le format de l'image
print("Taille de l'image :", img_a.size)
print("Format de l'image :", img_a.format)

# 3) Obtenir et afficher la valeur du pixel de coordonnée (400,250)
img_a=np.array(img_a)
pixel_value = img_a[400,250]
print("Valeur du pixel à la coordonnée (400,250) :", pixel_value)

# 4) Modifier la valeur du pixel pour qu'elle soit égale à (250, 250, 250)
img_a[400,250]=(250, 250, 250)

# 5) Enregistrer l'image sous le nom "M.jpg"
img_a=Image.fromarray(img_a)
img_a.save("M.jpg")

# 6) Afficher l'image avec Python
img_a.show()



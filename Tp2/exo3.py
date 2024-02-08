# Exercice 3 :
# En utilisant l’’image R.jpg, écrire un script python en utilisant la bibliothèque PIL pour :
# 1. Appliquer une symétrie par rapport à la moitié des lignes de l’image R
# 2. Appliquer une symétrie par rapport à la moitié des colonnes de l’image R
# 3. Appliquer une rotation de 90° de l’image R.jpg.


from PIL import Image
import numpy as np

# Charger l'image R.jpg
image_R = Image.open("Tp2/R.jpg")    
image_R = np.array(image_R)
nbligne,nbcolonne, _ = image_R.shape

symmetry_horizontal = np.zeros((nbligne, nbcolonne,3), dtype = 'uint8')

symmetry_vertical = np.zeros((nbligne, nbcolonne,3), dtype = 'uint8')

rotation_90_degrees = np.zeros((nbcolonne,nbligne,3), dtype = 'uint8')


for i in range(nbligne):
    for j in range(nbcolonne):

        # 1. Appliquer une symétrie par rapport à la moitié des lignes
        
        symmetry_horizontal[nbligne - i - 1, j] = image_R[i,j]

        # 2. Appliquer une symétrie par rapport à la moitié des colonnes

        symmetry_vertical[i, nbcolonne - j - 1] = image_R[i,j]

        # 3. Appliquer une rotation de 90°

        rotation_90_degrees[j, nbligne - i - 1] = image_R[i,j] # -i est (nbligne - i - 1)
        

# Afficher les images résultantes
Image.fromarray(symmetry_horizontal).show()
Image.fromarray(symmetry_vertical).show()
Image.fromarray(rotation_90_degrees).show()
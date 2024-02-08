from PIL import Image
import numpy as np

# Étape 1: Calculer la matrice (E) à partir de la matrice (A)
n=2
matrice_A = np.array([[1, 2], [3, 4]])
matrice_E = np.zeros((matrice_A.shape[0] * n, matrice_A.shape[1] * n))

for i in range(matrice_A.shape[0]): 
    for j in range(matrice_A.shape[1]):

        matrice_E[n*i : n*i + n, n*j : n*j + n] = matrice_A[i, j]

print(matrice_E)



# Étape 2: Appliquer ce principe de mise en échelle sur l'image R.jpg

def redimensione(matrice,n):
    e = np.zeros((matrice.shape[0] * n, matrice.shape[1] * n))
    
    for i in range(matrice.shape[0]): 
        for j in range(matrice.shape[1]):
            e[n*i : n*i + n, n*j : n*j + n] = matrice[i, j]
    
    return Image.fromarray(e)

image_R = Image.open('Tp2/R.jpg')
image_R=np.array(image_R)
print(image_R)

image_redimensionnee=redimensione(image_R,1)
image_redimensionnee.show()
image_redimensionnee.save('R_agrandi.jpg')

print("L'image a été agrandie avec succès et sauvegardée sous le nom 'R_agrandi.jpg'")


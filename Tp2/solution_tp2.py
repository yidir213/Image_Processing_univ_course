import numpy as np
from PIL import Image

a = np.array([[1,2,5], [3, 4,8]])
        
def ex01(a,n):
    e = np.zeros((a.shape[0] * n, a.shape[1] * n))
    
    for i in range(a.shape[0]): 
        for j in range(a.shape[1]):
            # e[2*i,2*j] = a[i, j] # e[0, 2] pour j = 1 avec a[0, 1] a la value 2
            # e[2*i,2*j + 1] = a[i, j] #  e[0, 3]
            # e[2*i + 1, 2*j] = a[i, j] #  e[1, 2]
            # e[2*i + 1, 2*j + 1] = a[i, j] #  e[1, 3]
            
            # e[2*i : 2*i + 2, 2*j : 2*j + 2] = a[i, j]
            e[n*i : n*i + n, n*j : n*j + n] = a[i, j]
            # e[i : i + n+1, j : j + n+1] = a[i, j]

    print(e)
    return e

def exo3():
    
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


# main(a, 2)
# main(a, 8)


ex01(a,2)

# matA=np.array([[1,2],[3,4]])
# matA= np.insert(matA, 1, [1,3],axis=1)
# print("Matrice A= ",matA)
# matC= np.insert(matA, 3, [2,4],axis=1)
# print("Matrice C= ",matC)
# matE= np.insert(matC, 0, [1,1,2,2],axis=0)
# print("Matrice E0= ",matE)
# matE= np.insert(matE, 2, [3,3,4,4],axis=0)
# print("Matrice E1= ",matE)
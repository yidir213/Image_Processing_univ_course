import numpy as np
import matplotlib as plt
from PIL import Image

def dialte(img, e):
    
    # matrix of zeros
    new = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    
    for i in range(e.shape[0]):
        for j in range(e.shape[1]):
            
            if e[i, j] == 1:
                
                for u in range(img.shape[0] - e.shape[0]):
                    for v in range(img.shape[1] - e.shape[1]):
                        if img[u,v] == 255:
                            new[u + i , v + j] = 255
                        
                            
    return new 

def histogramme_normalis(image):
    hist, _ = np.histogram(image.ravel(), bins = 256, range=[0,255])
    
    pi = hist / image.size # nombre de pixel
    
    return pi

def formule_p1(pi,k):  # P1(k)= Somme(pi)   i --> {0....k}
    
    p1 = np.sum(pi[:k]) # de 0 à k 
    #  or 
    p1 = 0
    for i in range(0, k):
        p1+=pi[i]  # p1 = p1 + pi[i]
    
    
    return p1

def formule_p2(pi,k): # P2(k)= Somme(pi)   i --> {k+1....L-1}
    
    p2 = np.sum(pi[k:])
    #  or 
    p2 = 0
    for i in range(k, 256): # de k à 255
        p2 += pi[i] # p2 = p2 + pi[i]
    
    
    return p2

def formule_m1(pi, k): # m1(k)= Somme(i*pi)/P1(k)  i --> {0....k}
    
    
    p1 = formule_p1(pi, k)
    
    if p1 <=0:
         return 0
     
    m1 = 0
    
    for i in range(0, k):
        
        m1+= i * pi[i]
    
    m1 = m1 / p1
    
    return m1

def formule_m2(pi, k):  # m2(k)= Somme(i*pi)/P2(k)  i --> {k+1....L-1}
    
    p2 = formule_p2(pi, k)
    
    if p2 <=0:
        return 0
    
    m2 = 0
    
    for i in range(k, 256):
        
        m2+= i * pi[i]
    
    m2 = m2 / p2
    
    return m2

def Otsu(image):
    
    pi = histogramme_normalis(image)
    
    #print(pi.shape) # 256 c'est le nombre max de niveau de gris 
    
    p1,p2,m1,m2 = np.zeros(256), np.zeros(256), np.zeros(256), np.zeros(256)
    mg, var = np.zeros(256), np.zeros(256)
    
    for k in range(0, 256):
        
        p1[k] = formule_p1(pi, k)
        p2[k] = formule_p2(pi, k)

        m1[k] = formule_m1(pi, k)
        m2[k] = formule_m2(pi, k)
        
        mg[k] = p1[k] * m1[k] + p2[k] * m2[k]
        
        var[k] = p1[k] * (m1[k] - mg[k]) ** 2 + p2[k] * (m2[k] - mg[k]) ** 2 
        
    print("le seuil k maximisant var est :", np.argmax(var), np.max(var), var[np.argmax(var)])
    
    k = np.argmax(var)
    
    return k
    

def seuillage(image,k):
    
    image[image < k ] = 0
    image[image >= k ] = 255
    
    return np.array(image, dtype='uint8')


# # Question 4 
# Lire L'image A
img_a = Image.open("TP6/A.jpg")

# Conertir L'image A au gris 
img_a_grey=img_a.convert('L')

# Conertir L'image A au matrice 
img_a_matrice = np.array(img_a_grey)

# Otsu pour trouver k
k = Otsu(img_a_matrice)

# Conertir L'image A au binaire (seuillage)
img_a_binaire = seuillage(img_a_matrice, k)

# Conertir la matrice au L'image A
Image.fromarray(img_a_binaire).show()

# e1
e1 = np.ones((7,7))

# dialting of the image A
img_a_dialted = dialte(img_a_binaire, e1)
Image.fromarray(img_a_dialted).show()


# Lire L'image B
img_b = Image.open("TP6/B.jpg")

# Conertir L'image B au gris 
img_b_grey=img_b.convert('L')

# Conertir L'image B au matrice 
img_b_matrice = np.array(img_b_grey)

# Otsu pour trouver k
k = Otsu(img_b_matrice)

# Conertir L'image B au binaire (seuillage)
img_b_binaire = seuillage(img_b_matrice, k)

# Conertir la matrice au L'image B
Image.fromarray(img_b_binaire).show()


# # Question 5
# Lire L'image B
img_b = Image.open("TP6/B.jpg")

# Les trois CANEAUX R,G,V
img_r, img_g, img_bl = img_b.split()

# Calcule la moyenne de k maximum

k_r = Otsu(np.array(img_r))

k_v = Otsu(np.array(img_g))

k_b = Otsu(np.array(img_bl))

k=(k_b + k_r + k_v)/3
print(k)

# Convertir L'image B au gris 
img_b_grey=img_b.convert('L')

# Convertir L'image B au matrice 
img_b_matrice = np.array(img_b_grey)

# Convertir L'image B au binaire (seuillage)
img_b_binaire = seuillage(img_b_matrice, k)

# Convertir la matrice au L'image B
Image.fromarray(img_b_binaire).show()



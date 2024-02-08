import numpy as np
from PIL import Image

import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage


#K--> modifier le contraste, 
#k>1 is used to increase the contrast
#0<k<1 is used to decrease the contrast
#k=1 is adjust the brightness of the image
# k=-1 et d=255, on obtient alors l'inverse de l'image


# #d --> modifier l'illumination


# 3. Appliquer la transformation linéaire des niveaux de gris
def transform_linear(image, k, d):
    
    image = np.array(image)
    
    image = np.array(k*image + d, dtype='uint8')

    # or
    
    # q1 = np.zeros((image.shape[0], image.shape[1]))
    
    # for i in range(image.shape[0]):
        
    #     for j in range(image.shape[1]):
            
    #         q1[i, j] = k * image[i,j] + d
            
    # image = np.array(q1, dtype='uint8')
    
    return Image.fromarray(image)

# 4. Calculer l'image inverse de (A)
def 𝐼𝑚𝑔𝐼𝑛𝑣𝑒𝑟𝑠𝑒(image):
    
    image = np.array(image)
    
    return Image.fromarray(255  - image)

# 5. Appliquer la transformation logarithmique
def log_transform(image):
    
    image = np.array(image)
   
    
    C = 255 / np.log(np.max(image)) # remettre l'intervalle de variation de c entre 0 et 255
    
    image = C * np.log(1 + image) # + 1 pour éviter le cas de log(0)
    
    image = np.array(image, dtype='uint8')
    
    return Image.fromarray(image)

# 6. Appliquer la correction de gamma
def correctiongamma(image, gamma, c = 255):
    
    image = np.array(image)
    # normaliser image sur 255 pour avoir l'intervalle [0,1]
    # multiplier par 255 pour intensités entre [0 255]
    image = image / c
    image = c*np.power(image, gamma)

    image = np.array(image, dtype='uint8')

    return Image.fromarray(image)


def ajustementcontraste(l,kmin = 0, kmax = 255):    

    ll = kmin + ((kmax - kmin) / (lmax - lmin)) * (l - lmin)
    
    return ll


# 1. Lire une image (A)
imgA = Image.open("Tp3/A.jpg")
imgA.show()

# 2. Afficher le format, les dimensions et le mode de représentation de l’image A.
print(imgA.format, imgA.size, imgA.mode)

# 3. Appliquer la transformation linéaire des niveaux de gris
imgA_linear_transformed = transform_linear(imgA,k=1,d=50)
imgA_linear_transformed.show()

# 4. Calculer l'image inverse de (A)
imgA_inverse = 𝐼𝑚𝑔𝐼𝑛𝑣𝑒𝑟𝑠𝑒(imgA)
imgA_inverse.show()

# 5. Appliquer la transformation logarithmique
imgB = Image.open("Tp3/B.jpg")
imgB_log = log_transform(imgB)
imgB_log.show()

# 6. Appliquer la correction de gamma
gamma_values = [0.2, 0.4, 1.5, 2.5]
gamma_images = [correctiongamma(imgB, gamma) for gamma in gamma_values]
for i, img in enumerate(gamma_images):
    img.save(f"gamma_img{i+1}.jpg")

# 7. Appliquer l’ajustement de contraste

r_intensity, g_intensity, b_intensity = imgA.split()


lmin,lmax = np.min(np.array(r_intensity)), np.max(np.array(r_intensity))
print("lmin,lmax de r : ",lmin,lmax)
r_intensity = r_intensity.point(ajustementcontraste) # la fonction point elle applique la fonction ajustementcontraste pour chaque pixel


lmin,lmax = np.min(np.array(g_intensity)), np.max(np.array(g_intensity))
print("lmin,lmax g : ",lmin,lmax)
g_intensity = g_intensity.point(ajustementcontraste)


lmin,lmax = np.min(np.array(b_intensity)), np.max(np.array(b_intensity))
print("lmin,lmax b : ",lmin,lmax)
b_intensity = b_intensity.point(ajustementcontraste)


new_img = Image.merge("RGB", (r_intensity, g_intensity, b_intensity))
new_img.show()

# 8. Tracer l’histogramme des trois canaux après l’ajustement de contraste.

fig,(ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(24,6))

ax1.set_xlabel("red value")
ax1.set_ylabel("Pixel count")
ax1.set_xlim([0, 255])
ax1.hist(np.array(r_intensity).ravel(), 256, [0,255], color = 'red')

ax2.set_xlabel("Green value")
ax2.set_ylabel("Pixel count")
ax2.set_xlim([0, 255])
ax2.hist(np.array(g_intensity).ravel(), 256, [0,255], color = 'green')

ax3.set_xlabel("Blue value")
ax3.set_ylabel("Pixel count")
ax3.set_xlim([0, 255])
ax3.hist(np.array(b_intensity).ravel(), 256, [0,255], color = 'blue')

plt.show()

# 9. Calculer l’histogramme cumulé des trois canaux après l’ajustement de contraste.




# image= Image.open("Tp3/C.jpg")
# print(image.size)
# image.show()

# r_intensity, g_intensity, b_intensity = image.split()


# img = Image.merge("RGB", (r_intensity, g_intensity, b_intensity))

# fig,(ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(24,6))

# ax1.set_xlabel("red value")
# ax1.set_ylabel("Pixel count")
# ax1.set_xlim([0, 255])
# ax1.hist(np.array(r_intensity).ravel(), 256, [0,255], color = 'red')

# ax2.set_xlabel("Green value")
# ax2.set_ylabel("Pixel count")
# ax2.set_xlim([0, 255])
# ax2.hist(np.array(g_intensity).ravel(), 256, [0,255], color = 'green')

# ax3.set_xlabel("Blue value")
# ax3.set_ylabel("Pixel count")
# ax3.set_xlim([0, 255])
# ax3.hist(np.array(b_intensity).ravel(), 256, [0,255], color = 'blue')

# plt.show()
# # fig.savefig("histogram1.png")








# img = Image.merge("RGB", (r_intensity, g_intensity, b_intensity))

# fig,(ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(24,6))

# ax1.set_xlabel("red value")
# ax1.set_ylabel("Pixel count")
# ax1.set_xlim([0, 255])
# ax1.hist(np.array(r_intensity).ravel(), 256, [0,255], color = 'red')

# ax2.set_xlabel("Green value")
# ax2.set_ylabel("Pixel count")
# ax2.set_xlim([0, 255])
# ax2.hist(np.array(g_intensity).ravel(), 256, [0,255], color = 'green')

# ax3.set_xlabel("Blue value")
# ax3.set_ylabel("Pixel count")
# ax3.set_xlim([0, 255])
# ax3.hist(np.array(b_intensity).ravel(), 256, [0,255], color = 'blue')

# plt.show()
# fig.savefig("histogram2.png")

# Image.open("histogram2.png").show()


    

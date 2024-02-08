# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:41:28 2023

@author: ait mehdi
"""

from PIL import Image
import  numpy as np

def exo1(): 

    try: 

        # 1) Ouvrir l'image
        img_a = Image.open("Tp1/A.jpg")

        # 2) Afficher la taille et le format de l'image
        print("Taille de l'image :", img_a.size)
        print("Format de l'image :", img_a.format)
        print("mode de l'image :", img_a.mode)

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

    except IOError: 
        print('image not found !')


def exo3():
    
    try: 

        # Load the image B et Convertir en array
        img_b = Image.open("Tp1/B.jpg")
        img_b=np.array(img_b)
        print(img_b)

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
        
    except IOError: 
        print('image not found !')
    

if __name__ == "__main__": 
    exo3()

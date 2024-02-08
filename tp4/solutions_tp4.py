import numpy as np 
from PIL import Image
import numpy as np
import scipy.ndimage



# 1. Read an image in color
image = Image.open("tp4/image.jpg")

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

img_inverse = 255 - np.array(img_gris)
img_inverse=Image.fromarray(img_inverse).show("Inverse Image")

# 7. Save the inverse image
img_inverse.save('tp5/ImgInverse.jpg')

# 8. Filter the images using the mentioned filters

a  = np.array(Image.open('tp4/imgbruit.png').convert('L'))

f_moyen = a


# Filtrer l'image avec filtre Median
def fmedian(a, k = 3):
    
    result = a
    
    for u in range(a.shape[0] - k):
        for v in range(a.shape[1] - k):
            f = a[u : u + k, v : v + k]
            f = a[u : u + k, v : v + k].ravel()
            f = np.sort(f)
            median = np.median(f)
            result[u + k // 2, v + k // 2] = median
            
    return Image.fromarray(np.array(result, dtype='uint8'))


# Show l'image avec filtre Median
fmedian(a).show()






# Filtrer l'image avec filtre Moyen
def fmean(a, k = 3):
    
    result = a
    
    for u in range(a.shape[0] - k):
        for v in range(a.shape[1] - k):
            mean = np.mean(a[u : u + k, v : v + k])
            result[u + k // 2, v + k // 2] = mean
            
    return Image.fromarray(np.array(result, dtype='uint8'))


# Show l'image avec filtre Median
fmean(a).show()





# Filtrer l'image avec filtre Moyen
def fmax(a, k = 3):
    
    result = a
    
    for u in range(a.shape[0] - k):
        for v in range(a.shape[1] - k):
            max_ = np.max(a[u : u + k, v : v + k])
            result[u + k // 2, v + k // 2] = max_
            
    return Image.fromarray(np.array(result, dtype='uint8'))

# Show l'image avec filtre max
fmax(a).show()




# Filtrer l'image avec filtre Moyen
def fmin(a, k = 3):
    
    result = a
    
    for u in range(a.shape[0] - k):
        for v in range(a.shape[1] - k):
            min_ = np.min(a[u : u + k, v : v + k])
            result[u + k // 2, v + k // 2] = min_
            
    return Image.fromarray(np.array(result, dtype='uint8'))



# Show l'image avec filtre min
fmin(a).show()

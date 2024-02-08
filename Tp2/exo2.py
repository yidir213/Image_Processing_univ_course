from PIL import Image

def interpolation_bilineaire(matrice, x, y):
    i = int(x)
    j = int(y)

    a = matrice[j][i]
    b = matrice[j][i+1]
    c = matrice[j+1][i]
    d = matrice[j+1][i+1]

    u = x - i
    v = y - j

    valeur = (1-u)*(1-v)*a + u*(1-v)*b + (1-u)*v*c + u*v*d
    return valeur

# Testons l'interpolation bilinéaire sur la matrice (A)
matrice_A = [
    [5, 6],
    [7, 8]
]
x, y = 0.09, 0.102
valeur_interpolee = interpolation_bilineaire(matrice_A, x, y)
print(f"Valeur interpolée à ({x}, {y}) dans la matrice A: {valeur_interpolee}")

# Appliquons l'interpolation bilinéaire à l'image R.jpg
image = Image.open('../B.jpg')
largeur, hauteur = image.size
nouvelle_largeur = int(largeur * 1.5)  # exemple de nouvelle taille
nouvelle_hauteur = int(hauteur * 1.5)

nouvelle_image = Image.new('RGB', (nouvelle_largeur, nouvelle_hauteur))

for j in range(nouvelle_hauteur):
    for i in range(nouvelle_largeur):
        x = i / (nouvelle_largeur / largeur)
        y = j / (nouvelle_hauteur / hauteur)
        r, g, b = image.getpixel((int(x), int(y)))
        nouvelle_image.putpixel((i, j), (int(r), int(g), int(b)))

nouvelle_image.save('R_interpole.jpg')
print("L'image interpolée a été sauvegardée sous le nom 'R_interpole.jpg'")
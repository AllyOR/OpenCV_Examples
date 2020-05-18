import cv2

src = cv2.imread("images/monedas4.jpg", 1)
img = cv2.imwrite("images/Original.png",src)
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# Aplicar suavizado Gaussiano
gauss = cv2.GaussianBlur(gray, (5,5), 0)
cv2.imwrite("images/Gauss.png", gauss)
thresh = 50 
		
# Detectar los bordes con un umbral min = 50 y max = 150 
canny_output = cv2.Canny(gray, thresh, thresh * 3)

# Mostrar los bordes detectados con Canny
cv2.imwrite("images/Bordes.png", canny_output)

# Buscar los contornos de la imagen, se almacenan en contours
contours,hierarchy = cv2.findContours(canny_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Mostrar la Imagen modificada por la funcion findContours
cv2.imwrite("images/Modificada.png", canny_output)

# Dibujar los contornos encontrados
print("\nObjetos encontrados: ", len(contours),"....")
for i in range(len(contours)):
    color = (255,0,0)
    cv2.drawContours(src, contours, -1, color, 2)

# Mostrar la imagen final
cv2.imwrite("images/Contornos.png", src)
print("\nFinalizado...")  
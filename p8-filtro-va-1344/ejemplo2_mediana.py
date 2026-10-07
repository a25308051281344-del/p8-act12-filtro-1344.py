
import cv2

# Cargar la imagen
imagen = cv2.imread("RESULTADO/TIBURON.jpg.png")

# Verificar que la imagen se haya cargado
if imagen is None:
    print("ERROR: No se pudo cargar la imagen.")
    exit()

print("Imagen cargada correctamente.")

# Aplicar filtro de mediana
imagen_filtrada = cv2.medianBlur(imagen, 5)

# Mostrar imágenes
cv2.imshow("Imagen original", imagen)
cv2.imshow("Imagen con filtro de mediana", imagen_filtrada)

# Guardar resultado
cv2.imwrite("RESULTADO/TIBURON_FILTRADA.jpg", imagen_filtrada)

print("Filtro de mediana aplicado correctamente.")
print("Resultado guardado en RESULTADO/TIBURON_FILTRADA.jpg")

# Esperar una tecla
cv2.waitKey(0)

# Cerrar ventanas
cv2.destroyAllWindows()


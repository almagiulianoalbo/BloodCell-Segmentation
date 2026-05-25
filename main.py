import cv2
import matplotlib.pyplot as plt

from preprocessing import cargar_imagen, preprocesar_imagen
from segmentation import segmentar_celulas


'''Significado de las imágenes mostradas
Imagen original: imagen microscópica real.
Escala de grises: simplificación de la imagen eliminando color.
Imagen suavizada: reducción de ruido con Gaussian Blur.
Contraste mejorado: células más resaltadas.
Threshold: separación binaria entre células y fondo.
Morfología: limpieza de ruido y mejora de regiones.
Distance Transform: detección de centros celulares.
Watershed final: separación automática de células pegadas.'''


def mostrar_resultados(imagen_original, gris, blur, ecualizada, thresh, apertura, distancia, imagen_watershed):
    imagen_rgb = cv2.cvtColor(imagen_original, cv2.COLOR_BGR2RGB)
    watershed_rgb = cv2.cvtColor(imagen_watershed, cv2.COLOR_BGR2RGB)

    titulos = [
        "Imagen original",
        "Escala de grises",
        "Imagen suavizada",
        "Contraste mejorado",
        "Threshold",
        "Morfología",
        "Distance Transform",
        "Watershed final"
    ]

    imagenes = [
        imagen_rgb,
        gris,
        blur,
        ecualizada,
        thresh,
        apertura,
        distancia,
        watershed_rgb
    ]

    plt.figure(figsize=(14, 8))

    for i in range(len(imagenes)):
        plt.subplot(2, 4, i + 1)
        plt.imshow(imagenes[i], cmap="gray")
        plt.title(titulos[i])
        plt.axis("off")

    plt.tight_layout()
    plt.show()


def main():
    ruta_imagen = "data/train/original/0a3b53c7-e7ab-4135-80aa-fd2079d727d6.jpg"

    imagen_original = cargar_imagen(ruta_imagen)

    gris, blur, ecualizada = preprocesar_imagen(imagen_original)

    thresh, apertura, distancia, marcadores, imagen_watershed = segmentar_celulas(
        imagen_original,
        ecualizada
    )

    cv2.imwrite("outputs/segmentacion_watershed.jpg", imagen_watershed)

    mostrar_resultados(
        imagen_original,
        gris,
        blur,
        ecualizada,
        thresh,
        apertura,
        distancia,
        imagen_watershed
    )


if __name__ == "__main__":
    main()




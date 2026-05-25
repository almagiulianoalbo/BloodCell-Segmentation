import cv2
import numpy as np


def segmentar_celulas(imagen_original, imagen_preprocesada):
    # Threshold automático con Otsu
    _, thresh = cv2.threshold(
        imagen_preprocesada,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Operaciones morfológicas para limpiar ruido
    kernel = np.ones((3, 3), np.uint8)

    apertura = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel,
        iterations=2
    )

    # Fondo seguro
    fondo_seguro = cv2.dilate(
        apertura,
        kernel,
        iterations=3
    )

    # Transformada de distancia para separar células pegadas
    distancia = cv2.distanceTransform(
        apertura,
        cv2.DIST_L2,
        5
    )

    # Primer plano seguro
    _, primer_plano = cv2.threshold(
        distancia,
        0.55 * distancia.max(),
        255,
        0
    )

    primer_plano = np.uint8(primer_plano)

    # Zona desconocida
    desconocido = cv2.subtract(fondo_seguro, primer_plano)

    # Connected components
    _, marcadores = cv2.connectedComponents(primer_plano)

    # Sumamos 1 para que el fondo no sea 0
    marcadores = marcadores + 1

    # Marcamos la zona desconocida como 0
    marcadores[desconocido == 255] = 0

    # Watershed
    imagen_watershed = imagen_original.copy()
    marcadores = cv2.watershed(imagen_watershed, marcadores)

    # Bordes del watershed en rojo
    imagen_watershed[marcadores == -1] = [0, 0, 255]
    # Máscara final limpia
    mascara_final = apertura.copy()

    # Obtener regiones segmentadas individuales
    regiones = []

    for etiqueta in np.unique(marcadores):

        # Ignorar fondo y bordes
        if etiqueta <= 1:
            continue

        mascara = np.zeros(imagen_original.shape[:2], dtype="uint8")
        mascara[marcadores == etiqueta] = 255

        regiones.append(mascara)

    return (
        thresh,
        apertura,
        distancia,
        marcadores,
        imagen_watershed,
        mascara_final,
        regiones
    )
    return thresh, apertura, distancia, marcadores, imagen_watershed

'''Este archivo contiene la segmentación y separación de células.

Pasos:
Threshold de Otsu: convierte la imagen en binaria separando células y fondo automáticamente.
Operaciones morfológicas: eliminan ruido y mejoran las formas celulares.
Dilatación: identifica regiones seguras del fondo.
Distance Transform: detecta los centros de las células midiendo distancia a los bordes.
Connected Components: asigna etiquetas a cada región detectada.
Watershed: separa células pegadas o superpuestas generando fronteras entre ellas.

Finalmente, los bordes detectados se marcan en rojo sobre la imagen original.

segmentacion_watershed.jpg: imagen final con bordes rojos del watershed.
mascara_final.jpg: máscara binaria limpia para que tu compañera use como base.
region_0.jpg, region_1.jpg, etc.: regiones/células separadas individualmente.

'''



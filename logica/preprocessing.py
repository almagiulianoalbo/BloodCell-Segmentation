import cv2
import numpy as np


def cargar_imagen(ruta):
    imagen = cv2.imread(ruta)

    if imagen is None:
        raise FileNotFoundError(f"No se pudo cargar la imagen: {ruta}")

    return imagen


def preprocesar_imagen(imagen):
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # Suavizado para reducir ruido
    blur = cv2.GaussianBlur(gris, (5, 5), 0)

    # Mejora de contraste
    ecualizada = cv2.equalizeHist(blur)

    return gris, blur, ecualizada



'''Este archivo realiza el preprocesamiento de la imagen para facilitar la detección de células.

Pasos:
Carga de imagen: se lee la imagen del dataset con OpenCV.
Escala de grises: se elimina la información de color para simplificar el análisis.
Gaussian Blur: se aplica un suavizado para reducir ruido y pequeñas imperfecciones.
Ecualización de histograma: se mejora el contraste para resaltar mejor las células respecto al fondo.

El objetivo de esta etapa es obtener una imagen más limpia y fácil de segmentar.'''
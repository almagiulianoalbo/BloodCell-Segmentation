# 🧫 BloodCell-Segmentation

Proyecto de Visión Artificial orientado al análisis automático de imágenes microscópicas de células sanguíneas mediante técnicas clásicas de procesamiento de imágenes y segmentación.

Desarrollado para la materia **Visión Artificial** — Ingeniería Biomédica.

---

# 📌 Objetivo del Proyecto

El objetivo principal es desarrollar un sistema capaz de:

- detectar células en imágenes microscópicas,
- contar automáticamente células sanguíneas,
- separar células superpuestas o pegadas,
- extraer características morfológicas,
- clasificar células según tamaño, forma o tipo,
- detectar posibles anomalías celulares.

El proyecto busca simular el funcionamiento básico de herramientas utilizadas en laboratorios biomédicos y sistemas de diagnóstico asistido por computadora.

---

# 🔬 Técnicas a utilizar

## Preprocesamiento
- Conversión a escala de grises
- Filtrado Gaussiano
- Mejora de contraste

## Segmentación
- Threshold adaptativo / Otsu
- Operaciones morfológicas
- Distance Transform
- Watershed

## Detección
- Contornos
- Connected Components
- Bounding Boxes

## Extracción de Features
- Área
- Perímetro
- Circularidad
- Relación ancho/alto
- Tamaño celular

## Clasificación
- Reglas basadas en features
- Machine Learning clásico (KNN / SVM / Random Forest)
- Posible extensión a Deep Learning

---

# 📂 Dataset Utilizado

## BCCD Dataset with Masks

Dataset de imágenes microscópicas de sangre periférica que contiene:

- glóbulos rojos (RBC),
- glóbulos blancos (WBC),
- plaquetas.

Además, incluye máscaras de segmentación, lo que permite validar resultados y entrenar modelos de clasificación.

---

# 🏗️ Estructura del Proyecto

```plaintext
BloodCellSegmentation/
│
├── data/
│   ├── test/
│   │   ├── mask/
│   │   └── original/
│   │
│   ├── train/
│   │   ├── mask/
│   │   └── original/
│
├── logica/
│   ├── classification.py
│   ├── features.py
│   ├── preprocessing.py
│   ├── segmentation.py
│   └── utils.py
│
├── outputs/
│
├── main.py
├── README.md
└── requirements.txt
```

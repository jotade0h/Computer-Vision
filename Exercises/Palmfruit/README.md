# 🧠 Inspección Visual de Fruta de Palma con YOLOv8

Este proyecto implementa un sistema de visión artificial para **inspección en tiempo real** de fruta de palma africana en una **banda transportadora**, utilizando el modelo **YOLOv8**.

## 🎯 Objetivo

Detectar y clasificar automáticamente los diferentes estados de maduración y condiciones de la fruta, con el fin de facilitar la evaluación rápida y precisa durante el proceso de poscosecha.

---

## 📸 Datos de entrada

El sistema parte de un **video capturado desde una banda transportadora** donde circulan frutos de palma con diferentes características:

- Fruta **verde**
- Fruta **madura**
- Fruta **sobremadura**
- Fruta **podrida**
- Fruta con **pedúnculo largo**

Se extrajeron imágenes representativas desde el video para construir un **dataset anotado manualmente**, cubriendo todas las categorías mencionadas.

---

## 🧰 Proceso

### 1. Extracción y anotación de imágenes

- Se extrajeron cuadros clave del video original.
- Las imágenes fueron etiquetadas utilizando [Roboflow](https://roboflow.com/) 
- Se definieron las clases para YOLO:
0: Verde
1: Madura
2: Sobremadura
3: Podrida
4: Pedúnculo largo


### 2. Entrenamiento del modelo


- Entrenamiento local

### 3. Inferencia en tiempo real

- Se reprodujo el video original para realizar la inspección en tiempo real.
- El modelo detecta y clasifica cada fruta, marcando su clase y posición.

---

## 📁 Estructura del repositorio

├── Data/ # Imágenes y etiquetas del dataset
├── Results\Frutadepalma\runs\detect # Pesos entrenados de YOLOv8
├── scripts/
│ ├── camera_stream.py # Script de inferencia en tiempo real
│ ├── train.py # Entrenamiento YOLO (opcional)
│ └── leer_env.py # Lectura de variables del .env
├── .env # Variables como CAMERA_URL (no subir a GitHub)
└── README.md # Este archivo
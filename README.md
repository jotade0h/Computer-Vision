---

## 🚆 Detección de Infraestructura y Elementos en Vías Férreas

El ejercicio ubicado en [`Ejercicios/Trenes`](./Ejercicios/Trenes) implementa un sistema avanzado de visión por computador basado en **YOLOv8** para la **detección y análisis de elementos críticos** en el entorno de vías férreas y carreteras.

### 🎯 Objetivo

Detectar, clasificar y **localizar automáticamente** elementos relevantes como vegetación, señales de tránsito, postes y basura. El sistema genera alertas al identificar objetos dentro de **zonas de prohibición** o áreas restringidas definidas por el usuario. Este enfoque permite facilitar:

- Mantenimiento preventivo (poda, limpieza)
- Verificación de infraestructura (señales, postes)
- Reportes automatizados de condiciones anómalas

---

### 🧠 Clases detectadas

- 🌿 **Vegetación invasiva**
- 🚯 **Basura o residuos sólidos**
- ⚠️ **Señales de tránsito**
- 🪵 **Postes (eléctricos o de señalización)**

---

### 🚨 Lógica de advertencia por zona

El sistema permite definir un área crítica o zona de advertencia dentro de cada imagen. Si uno o más objetos aparecen dentro de esta zona, se genera una advertencia visual y puede activarse un proceso de registro de incidencia.

🗺️ Estas incidencias pueden ser asociadas a coordenadas o posiciones relativas, para su **almacenamiento, análisis posterior o envío a sistemas de gestión operativa** (cuadrillas de mantenimiento, bases de datos, dashboards, etc.).

---

### 🧪 Técnicas utilizadas

- Entrenamiento de modelo YOLOv8 con dataset personalizado.
- Definición dinámica de **zonas de exclusión o advertencia**.
- Registro automatizado de objetos detectados en zonas críticas.
- Posible integración con backend o sistema de notificación.
  


---

## 🌴 Visión Computacional para Clasificación de Fruta de Palma Africana

El ejercicio ubicado en [`Ejercicios/Frutadepalma`](./Ejercicios/Frutadepalma) implementa un sistema de inspección visual automática para fruta de palma africana (*Elaeis guineensis*) utilizando algoritmos de visión por computador y detección en tiempo real con **YOLOv8**.

### 🎯 Objetivo

Automatizar el proceso de evaluación de calidad de los frutos en una **banda transportadora industrial**, clasificando en tiempo real distintos estados de maduración y condiciones visibles del fruto.

### 🔍 Categorías detectadas

El modelo fue entrenado para identificar las siguientes clases:

- 🟢 **Fruta verde**
- 🟠 **Fruta madura**
- 🔴 **Fruta sobremadura**
- ⚫ **Fruta podrida**
- 🧵 **Fruta con pedúnculo largo**

### 🧪 Detalles técnicos

- 📹 Imágenes extraídas desde video industrial real de la línea de producción.
- 🧾 Anotaciones realizadas manualmente usando herramientas como Roboflow.
- 🤖 Entrenamiento con [YOLOv8](https://github.com/ultralytics/ultralytics) en formato YOLOv5-compatible.
- 📦 Carpeta incluye modelos, scripts de inferencia, y sets de imágenes anotadas.

---

## 🧪 Ejercicios de visión por computador

Dentro de la carpeta [`Ejercicios/`](./Ejercicios/) se encuentran desarrolladas tres soluciones prácticas aplicadas a problemas reales de visión por computador. Cada punto está documentado en el archivo `Soluciones.pdf`, acompañado por sus respectivas carpetas de implementación:

---

### 🔷 Punto 1: Inspección de fugas de gas con cámaras OGI

Se aborda la inspección de gases invisibles al ojo humano mediante imágenes obtenidas por una cámara OGI (Optical Gas Imaging).  
El objetivo es **estimar el volumen de gas perdido** (propano) en cada imagen, comparando imágenes con fuga visible frente a imágenes sin fuga.

📁 Carpeta: `Ejercicios/Punto_1`  
🧠 Técnicas: procesamiento de imágenes, segmentación, análisis de diferencia de píxeles.

---

### 🔷 Punto 2: Inspección de galletas con o sin crema

Una fábrica desea detectar si la crema ha sido aplicada correctamente en galletas tipo sándwich.  
Se implementa un algoritmo que diferencia entre galletas con crema suficiente y bien ubicada (“Bueno”) frente a galletas sin crema o mal aplicadas (“Incorrecto”).

📁 Carpeta: `Ejercicios/Punto_2`  
📄 Contiene imágenes reales infrarrojas en carpetas “Bueno” e “Incorrecto”, así como scripts como `Punto_2_1.py`, `Punto_2_2.py` y `rgb.py`.

🧠 Técnicas: binarización, detección de contornos, área de segmentación.

---

### 🔷 Punto 3: Detección de placa y velocidad en infracción vehicular

Una cámara de seguridad capta una infracción cometida por un taxi.  
Se requiere identificar la **placa del taxi** (a pesar de estar borrosa por movimiento) y calcular la **velocidad aproximada** al momento de la captura.

📁 Carpeta: `Ejercicios/Punto_3`  
🧠 Técnicas: estimación de desenfoque por movimiento, OCR (reconocimiento de caracteres), procesamiento de imágenes.

---

📄 Toda la documentación teórica y explicativa está disponible en [`Ejercicios/Soluciones.pdf`](./Ejercicios/Soluciones.pdf), donde se detallan los pasos, algoritmos aplicados, ejemplos visuales y estructuras de carpetas para cada ejercicio.


---





## 🎥 Ejemplo Visual

<!-- Puedes reemplazar esto por una imagen real del proyecto -->
![Ejemplo detección](docs/ejemplo_deteccion.gif)

---

## 🧪 Características principales

- 🔍 Detección de múltiples clases: madura, verde, sobremadura, podrida, pedúnculo largo.
- 🚀 Modelo YOLOv8 entrenado con imágenes reales.
- 📦 Dataset personalizado generado a partir de video industrial.
- 🎥 Detección en tiempo real desde cámara IP.
- ⚙️ Flujo completo desde captura hasta despliegue en producción.

---

## 📁 Estructura del Repositorio


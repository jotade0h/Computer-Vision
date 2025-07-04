---

## 🚆 Infrastructure and Trackside Object Detection using YOLOv8

The exercise located in [`Exercises/Trains`](./Exercises/Trains) presents an advanced computer vision system based on **YOLOv8**, designed for the detection and analysis of critical elements surrounding railway tracks and roadways.

### 🎯 Objective

Automatically detect, classify, and **locate relevant objects** such as vegetation, traffic signs, utility poles, and litter. The system raises alerts when any of these objects are detected within **predefined exclusion zones** or critical areas. This functionality enables:

- Preventive maintenance (e.g., pruning, debris removal)
- Infrastructure verification (e.g., presence of signs and poles)
- Automated reporting of anomalies for decision support

---

### 🧠 Detected Classes

- 🌿 **Overgrown vegetation**
- 🚯 **Litter or solid waste**
- ⚠️ **Traffic signage**
- 🪵 **Utility or support poles**

---

### 🚨 Zone-Based Warning Logic

A dynamic exclusion zone can be defined in each frame. If any object is detected within this region, a warning is triggered, and the incident can be recorded.

🗺️ Detected incidents may be linked to spatial coordinates or relative positions for **reporting, analysis, or dispatching of operational response teams** (e.g., for cleanup, pruning, or repairs).

---

### 🧪 Technical Highlights

- YOLOv8 custom training with annotated datasets
- Dynamic warning area definition per frame
- Automated logging of detections within critical zones
- Optional integration with backend systems for alerts or storage

---

## 🌴 Computer Vision for Oil Palm Fruit Maturity Classification

The exercise located in [`Exercises/Palmfruit`](./Exercises/Palmfruit) implements an automated visual inspection system for African oil palm fruit (*Elaeis guineensis*), using real-time object detection powered by **YOLOv8**.

### 🎯 Objective

Automate quality control on an **industrial conveyor line** by classifying fruits based on ripeness and visible defects in real time.

### 🔍 Target Classes

The model was trained to identify the following categories:

- 🟢 **Unripe fruit**
- 🟠 **Ripe fruit**
- 🔴 **Overripe fruit**
- ⚫ **Rotten fruit**
- 🧵 **Fruit with elongated stalk (peduncle)**

---

### 🧪 Technical Details

- 📹 Frames extracted from real industrial video footage
- 🧾 Manual annotation using tools like Roboflow
- 🤖 Training with [YOLOv8](https://github.com/ultralytics/ultralytics) in YOLOv5-compatible format
- 📦 Folder contains trained models, inference scripts, and labeled datasets

---

## 🧪 Computer Vision Exercises

Within the [`Exercises/`](./Exercises/) directory, three practical exercises are implemented to address real-world computer vision challenges. Each problem is documented in `Soluciones.pdf` and includes a dedicated subfolder with its implementation:

---

### 🔷 Exercise 1: Gas Leak Inspection with OGI Cameras

Uses Optical Gas Imaging (OGI) to analyze gas leaks that are invisible to the human eye.  
The goal is to **quantify the volume of gas lost** (e.g., propane) by comparing images with and without visible gas presence.

📁 Folder: `Exercises/Punto_1`  
🧠 Techniques: image differencing, segmentation, pixel-wise analysis.

---

### 🔷 Exercise 2: Cream Detection in Sandwich Cookies

A quality control system is implemented to verify whether sandwich cookies have adequate and correctly placed cream.  
The algorithm distinguishes between **correctly filled cookies** (“Bueno”) and **defective ones** (“Incorrecto”).

📁 Folder: `Exercises/Punto_2`  
📄 Contains grayscale infrared images and Python scripts like `Punto_2_1.py`, `Punto_2_2.py`, and `rgb.py`.

🧠 Techniques: binarization, contour detection, area filtering.

---

### 🔷 Exercise 3: Vehicle Infraction - Plate and Speed Estimation

A security camera captures a taxi committing an infraction.  
The task involves extracting the **license plate number**, despite motion blur, and estimating the **vehicle's speed** at the time of the capture.

📁 Folder: `Exercises/Punto_3`  
🧠 Techniques: motion blur estimation, OCR (Optical Character Recognition), image processing.

---

📄 All supporting documentation, algorithms, and implementation details are provided in [`Exercises/Soluciones.pdf`](./Exercises/Soluciones.pdf).

---

## 🎥 Visual Example

<!-- Replace with an actual sample -->
![Detection Example](docs/ejemplo_deteccion.gif)

---

## 🧪 Key Features

- 🔍 Multi-class detection: ripe, unripe, overripe, rotten, peduncled fruits
- 🚀 YOLOv8 model trained on real data
- 📦 Custom dataset from industrial video footage
- 🎥 Real-time inference from IP camera feed
- ⚙️ Complete workflow: data acquisition, training, and deployment

---

## 📁 Repository Structure


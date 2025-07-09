![Gas Detection Example](Computer-Vision/Data/Exercises-Images/diferencia-ndvi-2025-2017.png)


🚆 Infrastructure and Trackside Object Detection using YOLOv8
The exercise located in Exercises/Trains presents an advanced computer vision system based on YOLOv8, designed for the detection and analysis of critical elements surrounding railway tracks and roadways.

🎯 Objective
Automatically detect, classify, and locate relevant objects such as vegetation, traffic signs, utility poles, and litter. The system raises alerts when any of these objects are detected within predefined exclusion zones or critical areas. This functionality enables:

Preventive maintenance (e.g., pruning, debris removal)

Infrastructure verification (e.g., presence of signs and poles)

Automated reporting of anomalies for decision support

🧠 Detected Classes
🌿 Overgrown vegetation

🚯 Litter or solid waste

⚠️ Traffic signage

🪵 Utility or support poles

🚨 Zone-Based Warning Logic
A dynamic exclusion zone is defined in each frame. If any object is detected within this region, a warning is triggered, and the incident can be recorded.

🗺️ Detected incidents can be linked to spatial coordinates or relative positions for reporting, analysis, or dispatching of operational response teams (e.g., for cleanup, pruning, or repairs).

🧪 Technical Highlights
- YOLOv8 custom training with annotated datasets

- Dynamic warning area definition per frame

- Automated logging of detections within critical zones

- Optional integration with backend systems for alerts or storage

📁 Resources and Results
The implementation scripts and additional processing tools can be found in the Exercises/Trains directory.
Some of the output results, including processed images and logs, are available in Results/Trains.

📹 The initial video used for detection can be accessed via a shared Google Drive link, which will be provided shortly.



  

---

🌴 Computer Vision for Oil Palm Fruit Maturity Classification
The exercise located in Exercises/Palmfruit implements an automated visual inspection system for African oil palm fruit (Elaeis guineensis), using real-time object detection powered by YOLOv8.

🎯 Objective
Automate quality control on an industrial conveyor line by classifying fruits based on ripeness and visible defects in real time.

🔍 Target Classes
The model was trained to identify the following categories:

🟢 Unripe fruit

🟠 Ripe fruit

🔴 Overripe fruit

⚫ Rotten fruit

🧵 Fruit with elongated stalk (peduncle)

🧪 Technical Details
📹 Frames extracted from real industrial video footage

🧾 Manual annotation using tools like Roboflow

🤖 Training with YOLOv8 in YOLOv5-compatible format

📦 Folder contains trained models, inference scripts, and labeled datasets

📁 Resources and Results
The input data, code, and training materials are located in Exercises/Palmfruit.

Output results such as labeled images, metrics, and detection logs can be found in Results/Palmfruit.

📹 Additional video results will be available via a Google Drive link, to be added later.


---

🧪 Computer Vision Exercises
Within the Exercises/ directory, three practical exercises are implemented to address real-world computer vision challenges. Each problem is documented in Soluciones.pdf and includes its own subfolder with code and data (results are stored in the /Results/ directory).

🔷 Exercise 1: Gas Leak Detection and Volume Estimation
A system for detecting invisible gas leaks using Optical Gas Imaging (OGI).
The objective is to detect the gas and quantify the volume leaked (e.g., propane) based on differences in infrared imagery.

📁 Results located in: Results/Punto_1
🧠 Techniques: image differencing, segmentation, pixel-wise volume estimation.

🔷 Exercise 2: Cream Detection in Sandwich Cookies
A visual quality control system for sandwich cookies.
The algorithm detects whether the cookies contain adequate cream filling and classifies them as “Bueno” or “Incorrecto”.

📁 Results located in: Results/Punto_2
🧠 Techniques: grayscale analysis, thresholding, contour detection, area filtering.

🔷 Exercise 3: Vehicle Speed and License Plate Recognition
A traffic camera captures a vehicle during an infraction.
The task involves estimating the vehicle’s speed and extracting the license plate despite motion blur.

📁 Results located in: Results/Punto_3
🧠 Techniques: motion blur analysis, OCR (Optical Character Recognition), plate localization, speed estimation via frame analysis.

📄 Full documentation, algorithms, and explanation of each approach can be found in Exercises/Soluciones.pdf.

🎥 Visual Example
<!-- Replace with an actual sample -->


🧪 Key Features
🔍 Multi-class detection: ripe, unripe, overripe, rotten, peduncled fruits

🚀 YOLOv8 model trained on real data

📦 Custom dataset from industrial video footage

🎥 Real-time inference from IP camera feed

⚙️ Complete workflow: data acquisition, training, and deployment


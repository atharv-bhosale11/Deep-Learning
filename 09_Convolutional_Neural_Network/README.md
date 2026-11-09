# 09. Convolutional Neural Networks (CNN)

This folder contains practical implementations and demonstrations of Convolutional Neural Networks (CNNs), covering convolution operations, edge detection, activation functions, pooling, flattening, fully connected layers, and real-time image classification.

## 📂 Programs

| Sr. No. | Program Name | Description |
|:---:|---|---|
| 01 | `01_CNN_Edge_Detection.py` | Demonstrates edge detection using a convolution operation and a custom kernel. |
| 02 | `02_CNN_Edge_Detection_Result_Display.py` | Visualizes CNN edge detection results using graphical matrix representations. |
| 03 | `03_CNN_Edge_Detection_Result_Animation.py` | Demonstrates step-by-step animated visualization of the convolution process. |
| 04 | `04_CNN_Edge_Detection_Cat.py` | Performs Canny edge detection on an image using OpenCV. |
| 05 | `05_Realtime_Image_Classification.py` | Performs real-time image classification using a webcam and the pre-trained MobileNetV2 model. |
| 06 | `06_CNN_Convolution_ReLU_Pooling_FC.py` | Demonstrates convolution, ReLU activation, max pooling, flattening, and fully connected layers with calculations. |
| 07 | `07_CNN_Convolution_ReLU_Pooling_FC_Graphical.py` | Provides animated graphical visualization of CNN convolution and pooling operations. |
| 08 | `08_CNN_Relu_Pooling_flattern.py` | Demonstrates CNN internal operations including ReLU, max pooling, flattening, and fully connected layers. |
| 09 | `09_CNN_Convolution_ReLU_Pooling_FC_Graphical_BigData.py` | Demonstrates CNN operations using larger input matrices, detailed convolution calculations, and graphical neural network visualization. |

## 🧠 Concepts Covered

- Convolution Operations
- Convolution Kernels and Feature Maps
- Edge Detection
- Canny Edge Detection
- ReLU Activation Function
- Max Pooling
- Flatten Layer
- Fully Connected Layer
- Weights and Bias
- CNN Architecture
- Feature Extraction
- Graphical CNN Visualization
- Animated Convolution and Pooling
- Real-Time Image Classification
- Transfer Learning
- MobileNetV2

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- OpenCV
- TensorFlow
- Keras
- MobileNetV2

## 📦 Prerequisites

Install the required libraries:

```bash
pip install numpy matplotlib opencv-python tensorflow
```

## ▶️ How to Run

Navigate to this directory:

```bash
cd 09_Convolutional_Neural_Network
```

Run any program:

```bash
python 01_CNN_Edge_Detection.py
```

Run real-time image classification:

```bash
python 05_Realtime_Image_Classification.py
```

**Note:** Real-time image classification requires a working webcam. MobileNetV2 downloads its pre-trained ImageNet weights when required.

For the OpenCV edge detection program, keep `sample.png` in the same directory as the Python file.

## 🎯 Learning Objectives

- Understand the fundamental architecture of CNNs.
- Learn how convolution extracts features from input images.
- Understand the role of activation functions such as ReLU.
- Learn how max pooling reduces feature map dimensions.
- Understand flattening and fully connected layers.
- Visualize internal CNN operations through graphical demonstrations.
- Perform edge detection using convolution and OpenCV.
- Implement real-time image classification using a pre-trained CNN model.

## 👨‍💻 Author

**Atharv Bhosale**

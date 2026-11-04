# 09. Convolutional Neural Network (CNN)

This folder contains practical implementations of Convolutional Neural Network (CNN) concepts, including convolution operations, edge detection, result visualization, animation, and real-time image classification using a pre-trained MobileNetV2 model.

## 📂 Programs

| Sr. No. | Program Name                                | Description                                                                                   |
| :-----: | ------------------------------------------- | --------------------------------------------------------------------------------------------- |
|    01   | `01_CNN_Edge_Detection.py`                  | Implements edge detection using a convolution operation with a manually defined kernel.       |
|    02   | `02_CNN_Edge_Detection_Result_Display.py`   | Visualizes the convolution process and resulting feature map using Matplotlib.                |
|    03   | `03_CNN_Edge_Detection_Result_Animation.py` | Demonstrates step-by-step animated CNN edge detection.                                        |
|    04   | `04_CNN_Edge_Detection_Cat.py`              | Implements Canny edge detection using OpenCV on an input image.                               |
|    05   | `05_Realtime_Image_Classification.py`       | Performs real-time image classification using a webcam and the pre-trained MobileNetV2 model. |

## 🧠 Concepts Covered

* Convolution Operations
* Convolution Kernels and Filters
* Feature Map Generation
* Edge Detection
* Step-by-Step Convolution Visualization
* Animated Convolution Process
* Canny Edge Detection
* OpenCV Image Processing
* Pre-trained CNN Models
* MobileNetV2 Architecture
* Image Preprocessing
* Real-Time Image Classification
* ImageNet Predictions

## 🛠️ Technologies Used

* Python
* NumPy
* Matplotlib
* OpenCV
* TensorFlow
* Keras
* MobileNetV2

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

For real-time image classification:

```bash
python 05_Realtime_Image_Classification.py
```

**Note:** The real-time classification program requires a working webcam. The MobileNetV2 model uses ImageNet weights, which may need to be downloaded on the first execution.

## 🎯 Learning Objectives

* Understand how convolution operations extract features from images.
* Learn how filters and kernels detect image edges.
* Visualize feature maps generated through convolution.
* Understand the working of Canny edge detection using OpenCV.
* Explore pre-trained CNN architectures through MobileNetV2.
* Implement real-time image classification using webcam input.

## 👨‍💻 Author

**Atharv Bhosale**

GitHub: [atharbhosale11](https://github.com/atharbhosale11)


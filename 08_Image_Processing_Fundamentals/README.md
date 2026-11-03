# 08. Image Processing Fundamentals

This folder contains Python implementations of fundamental image processing concepts using Pillow and NumPy.

These programs demonstrate how digital images are represented as pixels, how images can be converted into grayscale, resized, and transformed into numerical arrays for further processing in Machine Learning and Deep Learning.

## 📂 Programs

| Sr. No. | Program                               | Description                                                                                             |
| ------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| 01      | `01_Convert28by28_Grayscale_Image.py` | Loads an image, converts it into grayscale, resizes it to 28×28 pixels, and saves the processed image.  |
| 02      | `02_Pixel_Grayscale_Display.py`       | Converts a grayscale image into a NumPy array and displays its dimensions and pixel intensity values.   |
| 03      | `03_Color_Image_Pixel_Display.py`     | Loads a colored image, resizes it to 28×28 pixels, and displays RGB pixel values and image information. |

## 🖼️ Sample Images

The following sample images are used in these programs:

| Image             | Description                                                              |
| ----------------- | ------------------------------------------------------------------------ |
| `digit.png`       | Original digit image used for grayscale conversion.                      |
| `digit_28x28.png` | Resized 28×28 grayscale digit image used for pixel intensity extraction. |
| `color.png`       | Colored image used for RGB pixel extraction.                             |

## 📚 Concepts Covered

### 1. Image Loading and Processing

* Loading images using Pillow.
* Understanding digital image representation.
* Resizing images to 28×28 pixels.
* Converting RGB images into grayscale.

### 2. Grayscale Image Processing

* Understanding grayscale images.
* Converting images into NumPy arrays.
* Displaying pixel intensity values.
* Understanding pixel values from 0 to 255.

### 3. Color Image Processing

* Understanding RGB color channels.
* Extracting individual pixel values.
* Accessing Red, Green, and Blue components.
* Displaying image dimensions and pixel matrices.

### 4. Image Representation in Deep Learning

* Understanding how computers represent images numerically.
* Representing images as multidimensional arrays.
* Understanding image height, width, and channels.
* Learning how image data is supplied as input to CNNs.

## 🛠️ Technologies & Libraries Used

* **Python** – Core programming language.
* **Pillow (PIL)** – Image loading, resizing, and grayscale conversion.
* **NumPy** – Numerical array representation and pixel operations.

## 📦 Prerequisites

Install the required Python libraries:

```bash
pip install Pillow numpy
```

## ▶️ How to Run

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the directory:

```bash
cd Deep-Learning/08_Image_Processing_Fundamentals
```

Run individual programs:

```bash
python 01_Convert28by28_Grayscale_Image.py
python 02_Pixel_Grayscale_Display.py
python 03_Color_Image_Pixel_Display.py
```

**Note:** Keep the required input images (`digit.png`, `digit_28x28.png`, and `color.png`) in the working directory before executing the respective programs.

## 🎯 Learning Objectives

* Understand the fundamentals of digital image processing.
* Learn how images are represented using pixels.
* Convert images into grayscale format.
* Resize images to 28×28 dimensions.
* Extract pixel intensity values using NumPy.
* Understand RGB color channels.
* Represent images as numerical arrays.
* Understand the importance of image preprocessing in CNNs.

## 👨‍💻 Author

**Atharv Bhosale**

Computer Engineering | Python | Machine Learning | Deep Learning

---

⭐ This folder is part of my **Deep Learning** repository, documenting my learning and implementation of fundamental image processing concepts used in Computer Vision and CNNs.


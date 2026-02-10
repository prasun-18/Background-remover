#  AI Background Remover (Streamlit App)

This project is a **web-based AI Background Remover** built using
**Python, Streamlit, and the `rembg` library**. It allows users to
upload an image and automatically removes the background using a deep
learning model.

------------------------------------------------------------------------

##  Features

-   Upload images (`.png`, `.jpg`, `.jpeg`)
-   Preview original image
-   Remove background using AI
-   Supports **CPU and GPU acceleration**
-   Simple and interactive web UI using Streamlit

------------------------------------------------------------------------

##  How It Works

1.  User uploads an image using the Streamlit interface.
2.  The image is read using **Pillow (PIL)**.
3.  The **`rembg` library** uses a deep learning segmentation model to
    detect the foreground.
4.  The background is removed and the processed image is displayed.

------------------------------------------------------------------------

##  Project Structure

 ├── app.py
 ├── requirements.txt 
 ├── README.md

------------------------------------------------------------------------

##  Requirements

streamlit\
Pillow\
rembg[gpu]\
rembg[cpu]

Use either GPU or CPU version, not both. Here we are using `rembg[gpu] `

------------------------------------------------------------------------

##  Modules Explained

### Streamlit

Used for building interactive web UI components like buttons, file
uploaders, and image display.

### Pillow

Handles image loading and processing.

### rembg

AI-powered background removal using U2Net deep learning model.

#### CPU Version

-   No GPU required
-   Slower but easy setup

#### GPU Version

-   Requires NVIDIA GPU & CUDA
-   Much faster performance

------------------------------------------------------------------------

##  Code Explanation

Imports required libraries:

``` python
import streamlit as st
from PIL import Image
from rembg import remove
```

The app uploads an image, displays it, removes background using AI, and
shows the result.

------------------------------------------------------------------------

##  How to Run

Create virtual environment:

``` bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

``` bash
pip install -r requirements.txt
```

Run app:

``` bash
streamlit run app.py
```

------------------------------------------------------------------------

##  Output

-   Transparent background image
-   PNG format recommended

------------------------------------------------------------------------

##  Author

Prasun Kumar

# 📸 Image Processor Project

This project is designed to process images by converting them to **JPEG format** and resizing them to **1080 x 1920 pixels**, making them perfect for Instagram stories.

---

## ✨ Features
- 🖼️ Converts all images to **JPEG format**.
- 📏 Resizes images to **1080 x 1920 pixels**.
- 📂 Processes multiple images in a directory.
- 🛠️ Handles exceptions gracefully:
  - 🚫 Skips unsupported file formats with a warning.
  - 📋 Logs errors for processing issues while continuing processing.
  - ⚠️ Handles unexpected errors without crashing.

---

## 🚀 Instructions

```
# Clone the repository
git clone https://github.com/https://github.com/IteratorInnovator/image-processor.git

cd image-processor

# Install dependencies in requirements.txt (ensure python3 is installed)
python3 -m pip install -r requirements.txt

# Run the script
python3 process_images.py <source_directory>
```
## 🖥️ Example
### 📂 Before running processed_images.py
```
source_directory/
├── image1.png 
├── image2.png       
├── textfile.txt    # Non-image files will not be processed
└── randomfile.cpp
```        
###  After running processed_images.py
```
source_directory/
├── processed_images/  # Processed images will be stored in processed_images directory
      ├── image1.jpeg  # Images are converted to jpeg and resized to 1080 x 1920 pixels
      └── image2.jpeg
├── image1.png 
├── image2.png       
├── textfile.txt 
└── randomfile.cpp
```

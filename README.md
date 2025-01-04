# Image Processor Project

This project is designed to process images by converting them to JPEG format and resizing them to 1080 x 1920 pixels, making them perfect for Instagram stories.

---

## Features
- Converts all images to **JPEG format**.
- Resizes images to **1080 x 1920 pixels**.
- Processes multiple images in a directory.
- Handles exceptions gracefully:
  - Skips unsupported file formats with a warning.
  - Logs errors for processing issues while continuing processing.
  - Handles unexpected errors without crashing.

---

## Instructions

```
# Clone the repository
git clone https://github.com/https://github.com/IteratorInnovator/image-processor.git

cd image-processor

# Install dependencies in requirements.txt
python3 -m pip install -r requirements.txt

# Run the script
python3 process_images.py <source_directory>
```




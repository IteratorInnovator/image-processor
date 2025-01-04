import sys
import os
import subprocess
from pathlib import Path
import logging
from PIL import Image, UnidentifiedImageError

def main():
    logging.basicConfig(filename="./logfile.log",
                        level=logging.INFO,
                        filemode='a',
                        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    try:
        if len(sys.argv) < 2: # No directory provided
            raise ValueError("No argument entered. Please provide a valid directory.")
        source_directory = sys.argv[1]
        source_path = Path(source_directory)
        destination_path = source_path / "processed_images"
        destination_path.mkdir(exist_ok=True, parents=False) # Create 'processed_images' directory to store processed images
        if source_path.exists() == False: # Path does not exist
            raise NotADirectoryError("Directory is invalid. Please provide a valid directory.")
        if source_path.is_dir() == False: # Path is not a directory
            raise NotADirectoryError("Provided path is not a directory. Please provide a valid directory.")
    except Exception as e: 
        logging.error(e)
    for file in source_path.iterdir():
        if file.is_file():
            try:
                with Image.open(file) as image:                
                    new_image = image.convert("RGB") # Ensure compatibility with JPEG
                    new_image = new_image.resize((1080,1920)) # Resize image to 1080 x 1920 pixels (aspect ratio 1:1)
                    destination_file = destination_path / f"{file.stem}.jpeg"
                    new_image.save(destination_file, format="JPEG", quality=90, optimize=True) # Save image to <source_directory>/processed_images/
                    logging.info(f"{file} successfully converted and resized. Saved to {destination_path}.")
            except UnidentifiedImageError as e: # Account for non-image files
                logging.warning(f"{file} is a non-image file. Processing skipped.")
            except Exception as e:             
                logging.error(e)
      
if __name__ == "__main__":
    main()
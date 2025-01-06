import os
import shutil
import logging

def copy_directory_content(src, dest):
    try:
        # Delete existing contents of the destination directory
        shutil.rmtree(dest)
        logging.info(f"Deleted existing contents of {dest}")
    except FileNotFoundError:
        pass

    os.makedirs(dest, exist_ok=True) 
    logging.info(f"Created destination directory: {dest}")

    for item in os.listdir(src):
        source_path = os.path.join(src, item)
        destination_path = os.path.join(dest, item)
        logging.info(f"Processing: {source_path}")

        if os.path.isfile(source_path):
            shutil.copy2(source_path, destination_path)
            logging.info(f'Copied file: {source_path} to {destination_path}')
        elif os.path.isdir(source_path):
            copy_directory_content(source_path, destination_path)




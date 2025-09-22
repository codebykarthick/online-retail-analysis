import requests

import os
import zipfile
import shutil

DATASET_URL = "https://archive.ics.uci.edu/static/public/352/online+retail.zip"
DATA_DIR = os.path.join(os.getcwd(), "data")
ZIP_FILE = "data.zip"


def download_raw_dataset(force = False, chunk_size: int=128) -> None:
    """Method to download raw dataset - XLSX file and place it in "data/" folder 
    for easy accessibility.

    Args:
        force (boolean, optional): Whether to force delete and redownload the dataset. Defaults to False.
        chunk_size (int, optional): The chunk size to write the downloaded zip. Defaults to 128.
    """
    if len(os.listdir(DATA_DIR)) != 0:
        if force == False:
            print("Dataset seems to already exist, please delete manually or use force option to redownload.")
            return
        else:
            print("Clearing data/ folder for re-setup.")
            shutil.rmtree(DATA_DIR)

    os.makedirs(DATA_DIR, exist_ok=True)
    print(f"Downloading dataset from: {DATASET_URL}")
    res = requests.get(DATASET_URL, stream=True)
    zip_path = os.path.join(DATA_DIR, ZIP_FILE)
    with open(zip_path, "wb") as f:
        for chunk in res.iter_content(chunk_size=chunk_size):
            f.write(chunk)
    
    print(f"Download complete! Extracting...")

    with zipfile.ZipFile(zip_path, 'r') as z:
        z.extractall(DATA_DIR)
    
    print("Extraction complete, cleaning up artifacts...")
    os.remove(zip_path)

    print("All done!")
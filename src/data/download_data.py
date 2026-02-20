import os
import requests
import zipfile
from pathlib import Path

def download_movielens_25m():
    """Download and extract MovieLens 25M dataset"""
    
    # URL for MovieLens 25M
    url = "https://files.grouplens.org/datasets/movielens/ml-25m.zip"
    
    # Create data directory
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    zip_path = data_dir / "ml-25m.zip"
    
    # Download
    print("Downloading MovieLens 25M dataset...")
    print(f"URL: {url}")
    print(f"This may take several minutes (250+ MB)...")
    
    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    
    with open(zip_path, 'wb') as f:
        downloaded = 0
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            downloaded += len(chunk)
            progress = (downloaded / total_size) * 100
            print(f"\rProgress: {progress:.1f}%", end='')
    
    print("\n\nExtracting files...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    
    print("✓ Dataset downloaded and extracted successfully!")
    print(f"Location: {data_dir / 'ml-25m'}")
    
    # Clean up zip file
    os.remove(zip_path)
    print("✓ Cleaned up zip file")

if __name__ == "__main__":
    download_movielens_25m()
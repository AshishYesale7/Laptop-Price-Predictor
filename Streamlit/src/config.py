import os
from pathlib import Path

class Config:
    # Project structure
    ROOT_DIR = Path(__file__).parent.parent
    MODEL_DIR = ROOT_DIR / "models"
    
    # Ensure model directory exists
    MODEL_DIR.mkdir(exist_ok=True)
    
    # Model paths
    MODEL_PATH = MODEL_DIR / "pipe.pkl"
    DATA_PATH = MODEL_DIR / "data.pkl"
    
    # Input options
    RAM_OPTIONS = [2, 4, 6, 8, 12, 16, 24, 32, 64]
    STORAGE_OPTIONS = [0, 128, 256, 512, 1024, 2048]
    RESOLUTIONS = [
        '1920x1080', '1366x768', '1600x900', '3840x2160',
        '3200x1800', '2880x1800', '2560x1600', '2560x1440',
        '2304x1440'
    ]
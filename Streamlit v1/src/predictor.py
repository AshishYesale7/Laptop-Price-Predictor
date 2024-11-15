import pickle
import numpy as np
from pathlib import Path
from typing import Dict, Any
from config import Config
from utils import calculate_ppi

class LaptopPricePredictor:
    def __init__(self):
        self._load_models()
        
    def _load_models(self) -> None:
        """Load the ML model and dataset."""
        try:
            with open(Config.MODEL_PATH, 'rb') as f:
                self.pipe = pickle.load(f)
            with open(Config.DATA_PATH, 'rb') as f:
                self.df = pickle.load(f)
        except FileNotFoundError as e:
            raise RuntimeError(f"Required model files not found: {e}")
        except pickle.UnpicklingError as e:
            raise RuntimeError(f"Error loading model files: {e}")
            
    def predict(self, features: Dict[str, Any]) -> int:
        """Predict laptop price based on given features."""
        try:
            # Calculate PPI
            ppi = calculate_ppi(features['resolution'], features['screen_size'])
            
            # Prepare features array
            query = np.array([
                features['company'],
                features['type'],
                features['ram'],
                features['weight'],
                1 if features['touchscreen'] == 'Yes' else 0,
                1 if features['ips'] == 'Yes' else 0,
                ppi,
                features['cpu'],
                features['hdd'],
                features['ssd'],
                features['gpu'],
                features['os']
            ], dtype=object)
            
            # Make prediction
            query = query.reshape(1, 12)
            predicted_price = int(np.exp(self.pipe.predict(query)))
            
            return predicted_price
            
        except Exception as e:
            raise RuntimeError(f"Prediction error: {str(e)}")
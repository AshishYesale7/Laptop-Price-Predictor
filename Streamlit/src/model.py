import pickle
import numpy as np

class LaptopPricePredictor:
    def __init__(self):
        self.pipe = pickle.load(open('pipe.pkl', 'rb'))
        self.df = pickle.load(open('data.pkl', 'rb'))
    
    def calculate_ppi(self, resolution, screen_size):
        x_res, y_res = map(int, resolution.split('x'))
        return ((x_res**2) + (y_res**2))**0.5/screen_size
    
    def predict_price(self, features):
        query = np.array(features, dtype=object)
        query = query.reshape(1, 12)
        return int(np.exp(self.pipe.predict(query)))
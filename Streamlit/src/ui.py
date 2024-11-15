import streamlit as st
from model import LaptopPricePredictor

class LaptopPredictorUI:
    def __init__(self):
        self.predictor = LaptopPricePredictor()
        
    def get_binary_input(self, value):
        return 1 if value == 'Yes' else 0
    
    def render(self):
        st.title("Laptop Price Predictor")
        
        # Input sections
        company = st.selectbox('Brand', self.predictor.df['Company'].unique())
        laptop_type = st.selectbox('Type', self.predictor.df['TypeName'].unique())
        ram = st.selectbox('Ram(in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
        weight = st.number_input("Weight of the laptop")
        
        # Display features
        touchscreen = st.selectbox('TouchScreen', ['NO', 'Yes'])
        ips = st.selectbox('IPS', ['NO', 'Yes'])
        screen_size = st.number_input('Screen Size')
        
        resolution = st.selectbox('Screen Resolution', [
            '1920x1080', '1366x768', '1600x900', '3840x2160', 
            '3200x1800', '2880x1800', '2560x1600', '2560x1440', 
            '2304x1440'
        ])
        
        # Hardware specs
        cpu = st.selectbox('CPU', self.predictor.df['Cpu brand'].unique())
        hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])
        ssd = st.selectbox('SSD(in GB)', [0, 8, 128, 256, 512, 1024])
        gpu = st.selectbox('GPU', self.predictor.df['Gpu brand'].unique())
        os = st.selectbox('Operating System', self.predictor.df['os'].unique())
        
        if st.button('Predict Price'):
            # Process inputs
            touchscreen_val = self.get_binary_input(touchscreen)
            ips_val = self.get_binary_input(ips)
            ppi = self.predictor.calculate_ppi(resolution, screen_size)
            
            # Create feature array
            features = [company, laptop_type, ram, weight, touchscreen_val,
                       ips_val, ppi, cpu, hdd, ssd, gpu, os]
            
            # Get prediction
            predicted_price = self.predictor.predict_price(features)
            st.title(f"Predicted Price is ₹ {predicted_price:,}")
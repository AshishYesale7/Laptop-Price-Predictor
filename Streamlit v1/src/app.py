import streamlit as st
from typing import Dict, Any
from predictor import LaptopPricePredictor
from config import Config

def create_feature_inputs(predictor: LaptopPricePredictor) -> Dict[str, Any]:
    """Create and return user input features."""
    features = {}
    
    with st.form("prediction_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            features['company'] = st.selectbox('Brand', predictor.df['Company'].unique())
            features['type'] = st.selectbox('Type', predictor.df['TypeName'].unique())
            features['ram'] = st.selectbox('RAM (GB)', Config.RAM_OPTIONS)
            features['weight'] = st.number_input(
                "Weight (kg)", 
                min_value=0.5, 
                max_value=5.0, 
                value=1.5,
                step=0.1
            )
            
        with col2:
            features['touchscreen'] = st.selectbox('TouchScreen', ['No', 'Yes'])
            features['ips'] = st.selectbox('IPS Display', ['No', 'Yes'])
            features['screen_size'] = st.number_input(
                'Screen Size (inches)', 
                min_value=10.0, 
                max_value=20.0, 
                value=15.6,
                step=0.1
            )
            features['resolution'] = st.selectbox('Screen Resolution', Config.RESOLUTIONS)
        
        col3, col4 = st.columns(2)
        
        with col3:
            features['cpu'] = st.selectbox('CPU', predictor.df['Cpu brand'].unique())
            features['hdd'] = st.selectbox('HDD (GB)', Config.STORAGE_OPTIONS)
            
        with col4:
            features['gpu'] = st.selectbox('GPU', predictor.df['Gpu brand'].unique())
            features['ssd'] = st.selectbox('SSD (GB)', Config.STORAGE_OPTIONS)
        
        features['os'] = st.selectbox('Operating System', predictor.df['os'].unique())
        
        submitted = st.form_submit_button("Predict Price")
        
        return features, submitted

def main():
    # Page config
    st.set_page_config(
        page_title="Laptop Price Predictor",
        page_icon="💻",
        layout="centered"
    )
    
    # Header
    st.title("💻 Laptop Price Predictor")
    st.write("Predict laptop prices using machine learning with 82% accuracy")
    
    try:
        # Initialize predictor
        predictor = LaptopPricePredictor()
        
        # Get user inputs
        features, submitted = create_feature_inputs(predictor)
        
        if submitted:
            try:
                # Make prediction
                price = predictor.predict(features)
                st.success(f"### Predicted Price: ₹{price:,}")
                
                # Show feature importance
                st.info("""
                Key factors affecting the prediction:
                - RAM and storage configuration
                - CPU and GPU specifications
                - Screen size and resolution
                - Brand reputation
                """)
                
            except Exception as e:
                st.error(f"Error during prediction: {str(e)}")
                
    except Exception as e:
        st.error(f"Error initializing predictor: {str(e)}")

if __name__ == "__main__":
    main()
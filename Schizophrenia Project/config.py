import os
from datetime import timedelta

class Config:
    """Application configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Model paths
    MODEL_DIR = 'models'
    SCALER_PATH = os.path.join(MODEL_DIR, 'scaler.pkl')
    SVM_MODEL_PATH = os.path.join(MODEL_DIR, 'svm_model.pkl')
    KNN_MODEL_PATH = os.path.join(MODEL_DIR, 'knn_model.pkl')
    RF_MODEL_PATH = os.path.join(MODEL_DIR, 'rf_model.pkl')
    NN_MODEL_PATH = os.path.join(MODEL_DIR, 'nn_model.h5')
    
    # Logging
    LOG_DIR = 'logs'
    LOG_FILE = os.path.join(LOG_DIR, 'app.log')
    
    # Session
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # Feature names
    FEATURE_NAMES = ['Age', 'Gender', 'Marital_Status', 'Fatigue', 'Slowing', 'Pain', 'Hygiene', 'Movement']
    
    # Feature ranges for validation
    FEATURE_RANGES = {
        'Age': (0, 120),
        'Gender': (0, 1),
        'Marital_Status': (0, 1),
        'Fatigue': (0, 10),
        'Slowing': (0, 10),
        'Pain': (0, 10),
        'Hygiene': (0, 10),
        'Movement': (0, 10)
    }

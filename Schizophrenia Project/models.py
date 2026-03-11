import pickle
import numpy as np
import logging
from config import Config

logger = logging.getLogger(__name__)

class ModelManager:
    """Manages all ML models for schizophrenia detection"""
    
    def __init__(self):
        self.scaler = None
        self.models = {}
        self.load_models()
    
    def load_models(self):
        """Load all trained models"""
        try:
            self.scaler = pickle.load(open(Config.SCALER_PATH, 'rb'))
            self.models['svm'] = pickle.load(open(Config.SVM_MODEL_PATH, 'rb'))
            self.models['knn'] = pickle.load(open(Config.KNN_MODEL_PATH, 'rb'))
            self.models['rf'] = pickle.load(open(Config.RF_MODEL_PATH, 'rb'))
            # Neural Network requires TensorFlow - skip if not available
            try:
                from tensorflow import keras
                self.models['nn'] = keras.models.load_model(Config.NN_MODEL_PATH)
                logger.info("All models including Neural Network loaded successfully")
            except ImportError:
                logger.warning("TensorFlow not available - Neural Network model disabled")
            except Exception as e:
                logger.warning(f"Could not load Neural Network model: {str(e)}")
        except Exception as e:
            logger.error(f"Error loading models: {str(e)}")
            raise
    
    def predict(self, features, model_type='rf'):
        """
        Make prediction using specified model
        
        Args:
            features: List of feature values
            model_type: Type of model to use ('svm', 'knn', 'rf', 'nn')
        
        Returns:
            dict: Prediction results with class and probability
        """
        try:
            features_array = np.array(features).reshape(1, -1)
            features_scaled = self.scaler.transform(features_array)
            
            if model_type == 'nn':
                if 'nn' not in self.models:
                    logger.warning("Neural Network not available, using Random Forest instead")
                    model_type = 'rf'
                else:
                    prediction_proba = self.models['nn'].predict(features_scaled, verbose=0)
                    pred_class = int(np.argmax(prediction_proba, axis=1)[0])
                    confidence = float(np.max(prediction_proba))
                    return {
                        'class': pred_class,
                        'confidence': confidence,
                        'model_used': model_type
                    }
            
            model = self.models.get(model_type, self.models['rf'])
            pred_class = int(model.predict(features_scaled)[0])
            
            if hasattr(model, 'predict_proba'):
                prediction_proba = model.predict_proba(features_scaled)
                confidence = float(np.max(prediction_proba))
            else:
                confidence = 1.0
            
            return {
                'class': pred_class,
                'confidence': confidence,
                'model_used': model_type
            }
        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            raise
    
    def predict_all_models(self, features):
        """Get predictions from all models"""
        results = {}
        available_models = ['svm', 'knn', 'rf']
        if 'nn' in self.models:
            available_models.append('nn')
        
        for model_type in available_models:
            try:
                results[model_type] = self.predict(features, model_type)
            except Exception as e:
                logger.error(f"Error with {model_type}: {str(e)}")
                results[model_type] = {'error': str(e)}
        return results

def get_recommendation(pred_class, confidence):
    """Get recommendation based on prediction"""
    recommendations = {
        0: {
            'status': 'Healthy',
            'message': 'No signs of schizophrenia detected.',
            'advice': 'Maintain regular checkups and a healthy lifestyle. Continue monitoring mental health.',
            'severity': 'low'
        },
        1: {
            'status': 'At Risk',
            'message': 'Some symptoms detected that may indicate schizophrenia.',
            'advice': 'Consult a mental health professional for proper evaluation. Early intervention is important.',
            'severity': 'medium'
        }
    }
    
    result = recommendations.get(pred_class, recommendations[0])
    result['confidence'] = f"{confidence * 100:.1f}%"
    return result

def validate_features(features_dict):
    """Validate input features"""
    errors = []
    
    for feature_name, value in features_dict.items():
        if feature_name not in Config.FEATURE_RANGES:
            continue
        
        min_val, max_val = Config.FEATURE_RANGES[feature_name]
        if not (min_val <= value <= max_val):
            errors.append(f"{feature_name} must be between {min_val} and {max_val}")
    
    return errors

# Initialize global model manager
model_manager = ModelManager()

import pytest
import numpy as np
from models import model_manager, validate_features, get_recommendation

class TestModelManager:
    """Test cases for ModelManager class"""
    
    def test_models_loaded(self):
        """Test that all models are loaded"""
        assert model_manager.scaler is not None
        assert 'svm' in model_manager.models
        assert 'knn' in model_manager.models
        assert 'rf' in model_manager.models
        assert 'nn' in model_manager.models
    
    def test_predict_rf(self):
        """Test Random Forest prediction"""
        features = [35, 0, 1, 5.5, 3.2, 2.1, 1.5, 2.8]
        result = model_manager.predict(features, 'rf')
        
        assert 'class' in result
        assert 'confidence' in result
        assert 'model_used' in result
        assert result['class'] in [0, 1]
        assert 0 <= result['confidence'] <= 1
    
    def test_predict_svm(self):
        """Test SVM prediction"""
        features = [35, 0, 1, 5.5, 3.2, 2.1, 1.5, 2.8]
        result = model_manager.predict(features, 'svm')
        
        assert result['class'] in [0, 1]
        assert result['model_used'] == 'svm'
    
    def test_predict_all_models(self):
        """Test prediction across all models"""
        features = [35, 0, 1, 5.5, 3.2, 2.1, 1.5, 2.8]
        results = model_manager.predict_all_models(features)
        
        assert len(results) == 4
        assert 'rf' in results
        assert 'svm' in results
        assert 'knn' in results
        assert 'nn' in results

class TestValidation:
    """Test cases for feature validation"""
    
    def test_valid_features(self):
        """Test validation with valid features"""
        features = {
            'Age': 35,
            'Gender': 0,
            'Marital_Status': 1,
            'Fatigue': 5.5,
            'Slowing': 3.2,
            'Pain': 2.1,
            'Hygiene': 1.5,
            'Movement': 2.8
        }
        errors = validate_features(features)
        assert len(errors) == 0
    
    def test_invalid_age(self):
        """Test validation with invalid age"""
        features = {
            'Age': 150,
            'Gender': 0,
            'Marital_Status': 1,
            'Fatigue': 5.5,
            'Slowing': 3.2,
            'Pain': 2.1,
            'Hygiene': 1.5,
            'Movement': 2.8
        }
        errors = validate_features(features)
        assert len(errors) > 0
        assert any('Age' in error for error in errors)
    
    def test_invalid_symptom_range(self):
        """Test validation with out-of-range symptom"""
        features = {
            'Age': 35,
            'Gender': 0,
            'Marital_Status': 1,
            'Fatigue': 15,
            'Slowing': 3.2,
            'Pain': 2.1,
            'Hygiene': 1.5,
            'Movement': 2.8
        }
        errors = validate_features(features)
        assert len(errors) > 0

class TestRecommendations:
    """Test cases for recommendation generation"""
    
    def test_healthy_recommendation(self):
        """Test recommendation for healthy prediction"""
        rec = get_recommendation(0, 0.95)
        assert rec['status'] == 'Healthy'
        assert rec['severity'] == 'low'
        assert 'confidence' in rec
    
    def test_at_risk_recommendation(self):
        """Test recommendation for at-risk prediction"""
        rec = get_recommendation(1, 0.85)
        assert rec['status'] == 'At Risk'
        assert rec['severity'] == 'medium'
        assert 'confidence' in rec

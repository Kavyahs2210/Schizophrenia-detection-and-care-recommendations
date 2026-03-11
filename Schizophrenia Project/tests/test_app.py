import pytest
import json
from app import app

@pytest.fixture
def client():
    """Create test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

class TestRoutes:
    """Test cases for Flask routes"""
    
    def test_home_page(self, client):
        """Test home page loads"""
        response = client.get('/')
        assert response.status_code == 200
        assert b'Schizophrenia Detection' in response.data
    
    def test_detection_page_get(self, client):
        """Test detection page GET request"""
        response = client.get('/detection')
        assert response.status_code == 200
        assert b'Age' in response.data
    
    def test_detection_page_post(self, client):
        """Test detection page POST request"""
        data = {
            'Age': 35,
            'Gender': 0,
            'Marital_Status': 1,
            'Fatigue': 5.5,
            'Slowing': 3.2,
            'Pain': 2.1,
            'Hygiene': 1.5,
            'Movement': 2.8,
            'model_type': 'rf'
        }
        response = client.post('/detection', data=data)
        assert response.status_code == 200
    
    def test_about_page(self, client):
        """Test about page loads"""
        response = client.get('/about')
        assert response.status_code == 200
        assert b'About' in response.data
    
    def test_history_page(self, client):
        """Test history page loads"""
        response = client.get('/history')
        assert response.status_code == 200

class TestAPI:
    """Test cases for API endpoints"""
    
    def test_api_predict(self, client):
        """Test API prediction endpoint"""
        data = {
            'features': {
                'Age': 35,
                'Gender': 0,
                'Marital_Status': 1,
                'Fatigue': 5.5,
                'Slowing': 3.2,
                'Pain': 2.1,
                'Hygiene': 1.5,
                'Movement': 2.8
            },
            'model_type': 'rf'
        }
        response = client.post('/api/predict',
                              data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert 'prediction_class' in json_data
        assert 'confidence' in json_data
    
    def test_api_predict_missing_features(self, client):
        """Test API with missing features"""
        data = {}
        response = client.post('/api/predict',
                              data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == 400
    
    def test_api_compare(self, client):
        """Test API compare endpoint"""
        data = {
            'features': {
                'Age': 35,
                'Gender': 0,
                'Marital_Status': 1,
                'Fatigue': 5.5,
                'Slowing': 3.2,
                'Pain': 2.1,
                'Hygiene': 1.5,
                'Movement': 2.8
            }
        }
        response = client.post('/api/compare',
                              data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert 'results' in json_data
        assert len(json_data['results']) == 4
    
    def test_api_invalid_features(self, client):
        """Test API with invalid feature values"""
        data = {
            'features': {
                'Age': 200,
                'Gender': 0,
                'Marital_Status': 1,
                'Fatigue': 5.5,
                'Slowing': 3.2,
                'Pain': 2.1,
                'Hygiene': 1.5,
                'Movement': 2.8
            }
        }
        response = client.post('/api/predict',
                              data=json.dumps(data),
                              content_type='application/json')
        assert response.status_code == 400

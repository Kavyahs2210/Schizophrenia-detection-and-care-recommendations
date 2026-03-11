from flask import Flask, render_template, request, jsonify, session
from models import model_manager, get_recommendation, validate_features
from config import Config
import logging
import os
from datetime import datetime

# Setup logging
if not os.path.exists(Config.LOG_DIR):
    os.makedirs(Config.LOG_DIR)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(Config.LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(Config)

# Store prediction history
prediction_history = []

@app.route('/')
def home():
    """Home page"""
    return render_template('home.html')

@app.route('/detection', methods=['GET', 'POST'])
def detection():
    """Detection page with form"""
    prediction = None
    recommendation = None
    all_results = None
    error = None

    if request.method == 'POST':
        try:
            # Extract features
            features_dict = {
                'Age': float(request.form['Age']),
                'Gender': int(request.form['Gender']),
                'Marital_Status': int(request.form['Marital_Status']),
                'Fatigue': float(request.form['Fatigue']),
                'Slowing': float(request.form['Slowing']),
                'Pain': float(request.form['Pain']),
                'Hygiene': float(request.form['Hygiene']),
                'Movement': float(request.form['Movement'])
            }
            
            # Validate features
            validation_errors = validate_features(features_dict)
            if validation_errors:
                error = '; '.join(validation_errors)
                return render_template('detection.html', error=error, feature_ranges=Config.FEATURE_RANGES)
            
            features = list(features_dict.values())
            model_type = request.form.get('model_type', 'rf')
            
            # Get prediction
            result = model_manager.predict(features, model_type)
            pred_class = result['class']
            confidence = result['confidence']
            
            # Get all model predictions for comparison
            all_results = model_manager.predict_all_models(features)
            
            # Generate recommendation
            recommendation = get_recommendation(pred_class, confidence)
            
            if pred_class == 0:
                prediction = "✅ Healthy"
            else:
                prediction = "⚠️ May have Schizophrenia"
            
            # Log prediction
            log_entry = {
                'timestamp': datetime.now().isoformat(),
                'features': features_dict,
                'prediction': pred_class,
                'confidence': confidence,
                'model': model_type
            }
            prediction_history.append(log_entry)
            logger.info(f"Prediction made: {log_entry}")
            
        except ValueError as e:
            error = "Invalid input values. Please check your entries."
            logger.error(f"Validation error: {str(e)}")
        except Exception as e:
            error = f"An error occurred: {str(e)}"
            logger.error(f"Prediction error: {str(e)}")

    return render_template('detection.html', 
                         prediction=prediction, 
                         recommendation=recommendation,
                         all_results=all_results,
                         error=error,
                         feature_ranges=Config.FEATURE_RANGES)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    try:
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({'error': 'Missing features in request'}), 400
        
        features_dict = data['features']
        model_type = data.get('model_type', 'rf')
        
        # Validate features
        validation_errors = validate_features(features_dict)
        if validation_errors:
            return jsonify({'error': validation_errors}), 400
        
        features = [
            features_dict.get('Age'),
            features_dict.get('Gender'),
            features_dict.get('Marital_Status'),
            features_dict.get('Fatigue'),
            features_dict.get('Slowing'),
            features_dict.get('Pain'),
            features_dict.get('Hygiene'),
            features_dict.get('Movement')
        ]
        
        # Get prediction
        result = model_manager.predict(features, model_type)
        recommendation = get_recommendation(result['class'], result['confidence'])
        
        response = {
            'prediction_class': result['class'],
            'confidence': result['confidence'],
            'model_used': result['model_used'],
            'recommendation': recommendation,
            'timestamp': datetime.now().isoformat()
        }
        
        logger.info(f"API prediction: {response}")
        return jsonify(response), 200
        
    except Exception as e:
        logger.error(f"API error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/compare', methods=['POST'])
def api_compare():
    """Compare predictions across all models"""
    try:
        data = request.get_json()
        
        if not data or 'features' not in data:
            return jsonify({'error': 'Missing features in request'}), 400
        
        features_dict = data['features']
        
        # Validate features
        validation_errors = validate_features(features_dict)
        if validation_errors:
            return jsonify({'error': validation_errors}), 400
        
        features = [
            features_dict.get('Age'),
            features_dict.get('Gender'),
            features_dict.get('Marital_Status'),
            features_dict.get('Fatigue'),
            features_dict.get('Slowing'),
            features_dict.get('Pain'),
            features_dict.get('Hygiene'),
            features_dict.get('Movement')
        ]
        
        # Get all predictions
        all_results = model_manager.predict_all_models(features)
        
        return jsonify({
            'results': all_results,
            'timestamp': datetime.now().isoformat()
        }), 200
        
    except Exception as e:
        logger.error(f"API compare error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def history():
    """View prediction history"""
    return render_template('history.html', history=prediction_history[-50:])

@app.route('/about')
def about():
    """About page"""
    return render_template('about.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    logger.error(f"Server error: {str(e)}")
    return render_template('500.html'), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

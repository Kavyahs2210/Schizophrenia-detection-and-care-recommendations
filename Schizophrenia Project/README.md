# Schizophrenia Detection System

An AI-powered web application for early detection of schizophrenia symptoms using multiple machine learning models.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- **Multiple ML Models**: Choose from Random Forest, SVM, KNN, or Neural Network
- **Interactive UI**: Modern, responsive web interface with real-time feedback
- **Model Comparison**: Compare predictions across all models simultaneously
- **Confidence Scores**: Get detailed probability distributions for each prediction
- **REST API**: Programmatic access for integration with other applications
- **Prediction History**: Track and review past predictions during your session
- **Input Validation**: Comprehensive validation with helpful error messages
- **Logging & Monitoring**: Track all predictions and system events

## Technology Stack

- **Backend**: Flask (Python)
- **ML Framework**: TensorFlow, Scikit-learn
- **Frontend**: HTML5, CSS3, JavaScript
- **Models**: Random Forest, SVM, KNN, Neural Network

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd schizophrenia-detection
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Create environment file:
```bash
cp .env.example .env
```

6. Edit `.env` and set your configuration (optional)

## Usage

### Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

### Using the Web Interface

1. Navigate to the Detection page
2. Select your preferred ML model
3. Enter patient information:
   - Age (0-120)
   - Gender (Male/Female)
   - Marital Status (Single/Married)
   - Symptom ratings (0-10 scale):
     - Fatigue
     - Psychomotor Slowing
     - Pain
     - Hygiene Issues
     - Movement Abnormalities
4. Click "Analyze" to get prediction
5. View results with confidence scores and recommendations

### Using the REST API

#### Single Prediction

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{
    "features": {
      "Age": 35,
      "Gender": 0,
      "Marital_Status": 1,
      "Fatigue": 5.5,
      "Slowing": 3.2,
      "Pain": 2.1,
      "Hygiene": 1.5,
      "Movement": 2.8
    },
    "model_type": "rf"
  }'
```

Response:
```json
{
  "prediction_class": 0,
  "confidence": 0.95,
  "model_used": "rf",
  "recommendation": {
    "status": "Healthy",
    "message": "No signs of schizophrenia detected.",
    "advice": "Maintain regular checkups and a healthy lifestyle.",
    "severity": "low",
    "confidence": "95.0%"
  },
  "timestamp": "2024-03-11T10:30:00"
}
```

#### Compare All Models

```bash
curl -X POST http://localhost:5000/api/compare \
  -H "Content-Type: application/json" \
  -d '{
    "features": {
      "Age": 35,
      "Gender": 0,
      "Marital_Status": 1,
      "Fatigue": 5.5,
      "Slowing": 3.2,
      "Pain": 2.1,
      "Hygiene": 1.5,
      "Movement": 2.8
    }
  }'
```

## Project Structure

```
schizophrenia-detection/
├── app.py                 # Main Flask application
├── models.py              # ML model management
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── README.md             # This file
├── models/               # Trained ML models
│   ├── scaler.pkl
│   ├── rf_model.pkl
│   ├── svm_model.pkl
│   ├── knn_model.pkl
│   └── nn_model.h5
├── static/               # Static files
│   └── style.css
├── templates/            # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── detection.html
│   ├── about.html
│   ├── history.html
│   ├── 404.html
│   └── 500.html
├── tests/                # Test files
│   ├── __init__.py
│   ├── test_app.py
│   └── test_models.py
└── logs/                 # Application logs
```

## Input Features

| Feature | Description | Range |
|---------|-------------|-------|
| Age | Patient's age | 0-120 |
| Gender | 0=Male, 1=Female | 0-1 |
| Marital Status | 0=Single, 1=Married | 0-1 |
| Fatigue | Level of tiredness | 0-10 |
| Slowing | Psychomotor slowing | 0-10 |
| Pain | Physical pain level | 0-10 |
| Hygiene | Self-care issues | 0-10 |
| Movement | Movement abnormalities | 0-10 |

## Available Models

### Random Forest (RF) - Recommended
- Ensemble learning method
- Balanced accuracy and interpretability
- Good for general use cases

### Support Vector Machine (SVM)
- Powerful classifier
- Effective for high-dimensional data
- Good generalization

### K-Nearest Neighbors (KNN)
- Instance-based learning
- Simple and intuitive
- Good for small datasets

### Neural Network (NN)
- Deep learning model
- Captures complex patterns
- Requires more data

## Testing

Run the test suite:

```bash
pytest
```

Run with coverage:

```bash
pytest --cov=. --cov-report=html
```

## Deployment

### Production Server

Use Gunicorn for production:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

### Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:

```bash
docker build -t schizophrenia-detection .
docker run -p 5000:5000 schizophrenia-detection
```

## Configuration

Edit `config.py` or set environment variables:

- `SECRET_KEY`: Flask secret key for sessions
- `MODEL_DIR`: Directory containing trained models
- `LOG_DIR`: Directory for application logs

## Logging

Logs are stored in the `logs/` directory:
- `app.log`: Application events and predictions
- Includes timestamps, prediction details, and errors

## Security Considerations

- Input validation on all user inputs
- CSRF protection (configure SECRET_KEY)
- No permanent storage of sensitive data
- Sanitized error messages
- Rate limiting recommended for production

## Limitations & Disclaimer

**IMPORTANT**: This tool is for educational and research purposes only.

- Should NOT be used as the sole basis for medical diagnosis
- Always consult qualified healthcare professionals
- Predictions are based on limited features
- Not a replacement for clinical evaluation
- Early detection requires professional assessment

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new features
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the documentation
- Review the API examples

## Acknowledgments

- Built with Flask and TensorFlow
- Uses Scikit-learn for ML models
- Inspired by mental health awareness initiatives

## Future Enhancements

- [ ] User authentication and profiles
- [ ] Database integration for persistent storage
- [ ] More ML models (XGBoost, LightGBM)
- [ ] Feature importance visualization
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Integration with EHR systems
- [ ] Advanced analytics dashboard

---

**Remember**: Mental health is important. If you or someone you know is struggling, please seek professional help.

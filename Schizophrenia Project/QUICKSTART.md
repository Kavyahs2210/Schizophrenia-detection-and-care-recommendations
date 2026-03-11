# Quick Start Guide

Get the Schizophrenia Detection System up and running in 5 minutes!

## Prerequisites

- Python 3.8 or higher installed
- pip package manager
- Internet connection (for downloading dependencies)

## Installation Steps

### Option 1: Automated Setup (Recommended)

#### Windows
```bash
# Double-click run.bat or execute in terminal:
run.bat
```

#### Linux/Mac
```bash
# Make script executable
chmod +x run.sh

# Run the script
./run.sh
```

### Option 2: Manual Setup

1. **Create Virtual Environment**
```bash
python -m venv venv
```

2. **Activate Virtual Environment**
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Create Directories**
```bash
# Windows
mkdir logs
mkdir models

# Linux/Mac
mkdir -p logs models
```

5. **Train Models** (if not already trained)
```bash
python train_all_models.py
```

6. **Run Application**
```bash
python app.py
```

## First Use

1. Open your browser and go to:
   ```
   http://localhost:5000
   ```

2. Click "Start Detection" on the home page

3. Fill in the form:
   - Select a model (Random Forest recommended)
   - Enter patient age
   - Select gender and marital status
   - Rate symptoms on 0-10 scale using sliders

4. Click "Analyze" to get prediction

5. View results with:
   - Prediction (Healthy or At Risk)
   - Confidence score
   - Recommendations
   - Comparison across all models

## Testing the API

### Using cURL

```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d "{\"features\": {\"Age\": 35, \"Gender\": 0, \"Marital_Status\": 1, \"Fatigue\": 5.5, \"Slowing\": 3.2, \"Pain\": 2.1, \"Hygiene\": 1.5, \"Movement\": 2.8}, \"model_type\": \"rf\"}"
```

### Using Python

```python
import requests

url = "http://localhost:5000/api/predict"
data = {
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
}

response = requests.post(url, json=data)
print(response.json())
```

## Running Tests

```bash
# Install test dependencies (if not already installed)
pip install pytest pytest-flask

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run with coverage
pytest --cov=. --cov-report=html
```

## Common Issues

### Issue: Models not found
**Solution**: Run `python train_all_models.py` to train models

### Issue: Port 5000 already in use
**Solution**: Change port in app.py or kill the process using port 5000
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# Linux/Mac
lsof -ti:5000 | xargs kill -9
```

### Issue: Module not found
**Solution**: Ensure virtual environment is activated and dependencies installed
```bash
pip install -r requirements.txt
```

### Issue: TensorFlow errors
**Solution**: Install compatible TensorFlow version
```bash
pip install tensorflow==2.15.0
```

## Next Steps

- Read the [README.md](README.md) for detailed documentation
- Check [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API reference
- Review [DEPLOYMENT.md](DEPLOYMENT.md) for production deployment
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Features Overview

### Web Interface
- Modern, responsive design
- Interactive form with range sliders
- Real-time validation
- Model comparison view
- Prediction history

### API Endpoints
- `/api/predict` - Single model prediction
- `/api/compare` - Compare all models
- Full REST API with JSON responses

### Available Models
- **Random Forest** (Recommended) - Best balance of accuracy and speed
- **SVM** - Good for high-dimensional data
- **KNN** - Simple and interpretable
- **Neural Network** - Captures complex patterns

## Support

- Check the [README.md](README.md) for detailed information
- Review [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for API usage
- Open an issue on GitHub for bugs or questions

## Important Reminder

This tool is for educational purposes only. Always consult qualified healthcare professionals for medical diagnosis and treatment.

---

Happy coding! 🚀

# API Documentation

Complete API reference for the Schizophrenia Detection System.

## Base URL

```
http://localhost:5000
```

## Authentication

Currently, no authentication is required. For production use, implement API keys or OAuth.

## Endpoints

### 1. Single Model Prediction

Make a prediction using a specific ML model.

**Endpoint**: `POST /api/predict`

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
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
```

**Parameters**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| features | object | Yes | Patient feature values |
| features.Age | float | Yes | Age (0-120) |
| features.Gender | int | Yes | 0=Male, 1=Female |
| features.Marital_Status | int | Yes | 0=Single, 1=Married |
| features.Fatigue | float | Yes | Fatigue level (0-10) |
| features.Slowing | float | Yes | Psychomotor slowing (0-10) |
| features.Pain | float | Yes | Pain level (0-10) |
| features.Hygiene | float | Yes | Hygiene issues (0-10) |
| features.Movement | float | Yes | Movement abnormalities (0-10) |
| model_type | string | No | Model to use: "rf", "svm", "knn", "nn" (default: "rf") |

**Success Response** (200 OK):
```json
{
  "prediction_class": 0,
  "confidence": 0.95,
  "model_used": "rf",
  "recommendation": {
    "status": "Healthy",
    "message": "No signs of schizophrenia detected.",
    "advice": "Maintain regular checkups and a healthy lifestyle. Continue monitoring mental health.",
    "severity": "low",
    "confidence": "95.0%"
  },
  "timestamp": "2024-03-11T10:30:00.123456"
}
```

**Error Response** (400 Bad Request):
```json
{
  "error": ["Age must be between 0 and 120", "Fatigue must be between 0 and 10"]
}
```

**Error Response** (500 Internal Server Error):
```json
{
  "error": "Model prediction failed"
}
```

**Example cURL**:
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

**Example Python**:
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
result = response.json()
print(result)
```

---

### 2. Compare All Models

Get predictions from all available models for comparison.

**Endpoint**: `POST /api/compare`

**Request Headers**:
```
Content-Type: application/json
```

**Request Body**:
```json
{
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
}
```

**Parameters**:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| features | object | Yes | Patient feature values (same as predict endpoint) |

**Success Response** (200 OK):
```json
{
  "results": {
    "rf": {
      "class": 0,
      "confidence": 0.95,
      "model_used": "rf"
    },
    "svm": {
      "class": 0,
      "confidence": 0.92,
      "model_used": "svm"
    },
    "knn": {
      "class": 0,
      "confidence": 0.88,
      "model_used": "knn"
    },
    "nn": {
      "class": 0,
      "confidence": 0.94,
      "model_used": "nn"
    }
  },
  "timestamp": "2024-03-11T10:30:00.123456"
}
```

**Error Response** (400 Bad Request):
```json
{
  "error": ["Age must be between 0 and 120"]
}
```

**Example cURL**:
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

**Example JavaScript**:
```javascript
const url = 'http://localhost:5000/api/compare';
const data = {
  features: {
    Age: 35,
    Gender: 0,
    Marital_Status: 1,
    Fatigue: 5.5,
    Slowing: 3.2,
    Pain: 2.1,
    Hygiene: 1.5,
    Movement: 2.8
  }
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
})
.then(response => response.json())
.then(result => console.log(result))
.catch(error => console.error('Error:', error));
```

---

## Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request - Invalid input |
| 404 | Not Found - Endpoint doesn't exist |
| 500 | Internal Server Error |

## Prediction Classes

| Class | Description |
|-------|-------------|
| 0 | Healthy - No signs of schizophrenia |
| 1 | At Risk - Symptoms detected |

## Model Types

| Code | Model Name | Description |
|------|------------|-------------|
| rf | Random Forest | Recommended for general use |
| svm | Support Vector Machine | Good for high-dimensional data |
| knn | K-Nearest Neighbors | Simple instance-based learning |
| nn | Neural Network | Deep learning model |

## Rate Limiting

Currently no rate limiting is implemented. For production:
- Recommended: 100 requests per minute per IP
- Implement using Flask-Limiter

## Error Handling

All errors return JSON with an `error` field:

```json
{
  "error": "Error message or array of validation errors"
}
```

## Best Practices

1. **Validate Input**: Always validate features before sending
2. **Handle Errors**: Implement proper error handling
3. **Use HTTPS**: In production, always use HTTPS
4. **Cache Results**: Cache predictions when appropriate
5. **Timeout**: Set reasonable timeout values (30s recommended)

## Integration Examples

### Python with Error Handling

```python
import requests
from typing import Dict, Any

def predict_schizophrenia(features: Dict[str, float], model_type: str = "rf") -> Dict[str, Any]:
    """
    Make a prediction using the API
    
    Args:
        features: Dictionary of patient features
        model_type: Model to use (rf, svm, knn, nn)
    
    Returns:
        Prediction result dictionary
    """
    url = "http://localhost:5000/api/predict"
    
    try:
        response = requests.post(
            url,
            json={"features": features, "model_type": model_type},
            timeout=30
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return {"error": str(e)}

# Usage
features = {
    "Age": 35,
    "Gender": 0,
    "Marital_Status": 1,
    "Fatigue": 5.5,
    "Slowing": 3.2,
    "Pain": 2.1,
    "Hygiene": 1.5,
    "Movement": 2.8
}

result = predict_schizophrenia(features)
if "error" not in result:
    print(f"Prediction: {result['prediction_class']}")
    print(f"Confidence: {result['confidence']}")
else:
    print(f"Error: {result['error']}")
```

### Node.js with Axios

```javascript
const axios = require('axios');

async function predictSchizophrenia(features, modelType = 'rf') {
  try {
    const response = await axios.post('http://localhost:5000/api/predict', {
      features: features,
      model_type: modelType
    }, {
      timeout: 30000
    });
    
    return response.data;
  } catch (error) {
    if (error.response) {
      console.error('API Error:', error.response.data);
      return { error: error.response.data.error };
    } else {
      console.error('Network Error:', error.message);
      return { error: error.message };
    }
  }
}

// Usage
const features = {
  Age: 35,
  Gender: 0,
  Marital_Status: 1,
  Fatigue: 5.5,
  Slowing: 3.2,
  Pain: 2.1,
  Hygiene: 1.5,
  Movement: 2.8
};

predictSchizophrenia(features)
  .then(result => {
    if (!result.error) {
      console.log('Prediction:', result.prediction_class);
      console.log('Confidence:', result.confidence);
    } else {
      console.log('Error:', result.error);
    }
  });
```

## Changelog

### Version 1.0.0 (2024-03-11)
- Initial API release
- Single prediction endpoint
- Model comparison endpoint
- Input validation
- Error handling

---

For questions or issues, please open a GitHub issue.

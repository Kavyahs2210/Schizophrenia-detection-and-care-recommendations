#!/bin/bash

# Schizophrenia Detection System - Run Script

echo "Starting Schizophrenia Detection System..."

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Virtual environment not found. Creating..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
mkdir -p logs
mkdir -p models

# Check if models exist
if [ ! -f "models/scaler.pkl" ]; then
    echo "Models not found. Please train models first:"
    echo "  python train_all_models.py"
    exit 1
fi

# Run the application
echo "Starting Flask application..."
python app.py

#!/usr/bin/env python
"""
Setup Verification Script
Checks if all components are properly configured
"""

import os
import sys
from pathlib import Path

def check_python_version():
    """Check Python version"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} (OK)")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} (Need 3.8+)")
        return False

def check_dependencies():
    """Check if required packages are installed"""
    print("\nChecking dependencies...")
    required = [
        'flask',
        'tensorflow',
        'sklearn',
        'numpy',
        'pandas'
    ]
    
    missing = []
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package}")
        except ImportError:
            print(f"✗ {package} (missing)")
            missing.append(package)
    
    return len(missing) == 0

def check_directories():
    """Check if required directories exist"""
    print("\nChecking directories...")
    required_dirs = ['models', 'static', 'templates', 'logs']
    
    all_exist = True
    for dir_name in required_dirs:
        if os.path.exists(dir_name):
            print(f"✓ {dir_name}/")
        else:
            print(f"✗ {dir_name}/ (missing)")
            all_exist = False
    
    return all_exist

def check_files():
    """Check if required files exist"""
    print("\nChecking core files...")
    required_files = [
        'app.py',
        'models.py',
        'config.py',
        'requirements.txt',
        'templates/base.html',
        'templates/home.html',
        'templates/detection.html',
        'static/style.css'
    ]
    
    all_exist = True
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} (missing)")
            all_exist = False
    
    return all_exist

def check_models():
    """Check if trained models exist"""
    print("\nChecking trained models...")
    model_files = [
        'models/scaler.pkl',
        'models/rf_model.pkl',
        'models/svm_model.pkl',
        'models/knn_model.pkl',
        'models/nn_model.h5'
    ]
    
    all_exist = True
    for model_file in model_files:
        if os.path.exists(model_file):
            size = os.path.getsize(model_file)
            print(f"✓ {model_file} ({size:,} bytes)")
        else:
            print(f"✗ {model_file} (missing)")
            all_exist = False
    
    if not all_exist:
        print("\n⚠ Models not found. Run: python train_all_models.py")
    
    return all_exist

def check_config():
    """Check configuration"""
    print("\nChecking configuration...")
    
    if os.path.exists('.env'):
        print("✓ .env file exists")
    else:
        print("⚠ .env file not found (optional)")
    
    if os.path.exists('.env.example'):
        print("✓ .env.example exists")
    else:
        print("✗ .env.example missing")
    
    return True

def test_imports():
    """Test if core modules can be imported"""
    print("\nTesting module imports...")
    
    try:
        import app
        print("✓ app.py imports successfully")
    except Exception as e:
        print(f"✗ app.py import failed: {e}")
        return False
    
    try:
        import models
        print("✓ models.py imports successfully")
    except Exception as e:
        print(f"✗ models.py import failed: {e}")
        return False
    
    try:
        import config
        print("✓ config.py imports successfully")
    except Exception as e:
        print(f"✗ config.py import failed: {e}")
        return False
    
    return True

def main():
    """Run all checks"""
    print("="*60)
    print("Schizophrenia Detection System - Setup Verification")
    print("="*60)
    
    checks = [
        ("Python Version", check_python_version),
        ("Dependencies", check_dependencies),
        ("Directories", check_directories),
        ("Core Files", check_files),
        ("Trained Models", check_models),
        ("Configuration", check_config),
        ("Module Imports", test_imports)
    ]
    
    results = []
    for name, check_func in checks:
        try:
            result = check_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ Error during {name} check: {e}")
            results.append((name, False))
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")
    
    print(f"\nTotal: {passed}/{total} checks passed")
    
    if passed == total:
        print("\n✅ All checks passed! System is ready to run.")
        print("\nTo start the application:")
        print("  python app.py")
        print("\nOr use the run scripts:")
        print("  Windows: run.bat")
        print("  Linux/Mac: ./run.sh")
        return 0
    else:
        print("\n⚠ Some checks failed. Please fix the issues above.")
        if not any(name == "Trained Models" and not result for name, result in results):
            print("\nTo install dependencies:")
            print("  pip install -r requirements.txt")
        return 1

if __name__ == "__main__":
    sys.exit(main())

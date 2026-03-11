# Schizophrenia Detection System - Documentation Index

Welcome to the complete documentation for the Schizophrenia Detection System v2.0!

## 📚 Documentation Overview

This project includes comprehensive documentation for users, developers, and maintainers. Use this index to find what you need quickly.

## 🚀 Getting Started

### For First-Time Users
1. **[QUICKSTART.md](QUICKSTART.md)** - Get up and running in 5 minutes
2. **[README.md](README.md)** - Complete project overview and features
3. **Run verification**: `python verify_setup.py`

### Quick Commands
```bash
# Setup and run (Windows)
run.bat

# Setup and run (Linux/Mac)
chmod +x run.sh && ./run.sh

# Manual setup
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python train_all_models.py  # If models don't exist
python app.py
```

## 📖 Core Documentation

### User Documentation
- **[README.md](README.md)** - Main documentation
  - Project overview
  - Features and capabilities
  - Installation instructions
  - Usage guide
  - Input features explanation
  - Model descriptions

- **[QUICKSTART.md](QUICKSTART.md)** - Quick start guide
  - 5-minute setup
  - First use walkthrough
  - Common issues and solutions
  - Testing instructions

### Developer Documentation
- **[API_DOCUMENTATION.md](API_DOCUMENTATION.md)** - Complete API reference
  - Endpoint specifications
  - Request/response formats
  - Error codes
  - Integration examples
  - Best practices

- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
  - How to contribute
  - Coding standards
  - Testing requirements
  - Pull request process
  - Development setup

### Deployment Documentation
- **[DEPLOYMENT.md](DEPLOYMENT.md)** - Production deployment guide
  - Local development setup
  - Production server configuration
  - Docker deployment
  - Cloud platform deployment (AWS, GCP, Azure, Heroku)
  - Security considerations
  - Monitoring and maintenance

### Project Information
- **[PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)** - Comprehensive project overview
  - What's new in v2.0
  - Complete project structure
  - Technology stack
  - Key features
  - Performance metrics
  - Future roadmap

- **[CHANGELOG.md](CHANGELOG.md)** - Version history
  - Release notes
  - New features
  - Bug fixes
  - Breaking changes
  - Upcoming features

- **[LICENSE](LICENSE)** - MIT License
  - Usage terms
  - Disclaimer
  - Legal information

## 🎯 Quick Reference by Task

### I want to...

#### Install and Run
→ Start with [QUICKSTART.md](QUICKSTART.md)
→ Then read [README.md](README.md) for details

#### Use the Web Interface
→ See "Usage" section in [README.md](README.md)
→ Check "First Use" in [QUICKSTART.md](QUICKSTART.md)

#### Use the API
→ Read [API_DOCUMENTATION.md](API_DOCUMENTATION.md)
→ See API examples in [README.md](README.md)

#### Deploy to Production
→ Follow [DEPLOYMENT.md](DEPLOYMENT.md)
→ Review security section in [README.md](README.md)

#### Contribute Code
→ Read [CONTRIBUTING.md](CONTRIBUTING.md)
→ Check [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for architecture

#### Understand the Project
→ Start with [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md)
→ Review [CHANGELOG.md](CHANGELOG.md) for history

#### Troubleshoot Issues
→ Check "Common Issues" in [QUICKSTART.md](QUICKSTART.md)
→ See "Troubleshooting" in [DEPLOYMENT.md](DEPLOYMENT.md)

## 📁 File Structure Reference

```
Documentation Files:
├── INDEX.md                    # This file - Documentation index
├── README.md                   # Main documentation
├── QUICKSTART.md              # Quick start guide
├── API_DOCUMENTATION.md       # API reference
├── DEPLOYMENT.md              # Deployment guide
├── CONTRIBUTING.md            # Contribution guidelines
├── PROJECT_SUMMARY.md         # Project overview
├── CHANGELOG.md               # Version history
└── LICENSE                    # License information

Application Files:
├── app.py                     # Main Flask application
├── models.py                  # ML model management
├── config.py                  # Configuration
├── train_all_models.py        # Model training
├── verify_setup.py            # Setup verification
├── requirements.txt           # Dependencies
├── .env.example              # Environment template
├── run.sh                    # Linux/Mac run script
└── run.bat                   # Windows run script

Frontend:
├── templates/                 # HTML templates
│   ├── base.html
│   ├── home.html
│   ├── detection.html
│   ├── about.html
│   ├── history.html
│   ├── 404.html
│   └── 500.html
└── static/
    └── style.css             # Styling

Testing:
├── tests/
│   ├── test_app.py           # Application tests
│   └── test_models.py        # Model tests
└── pytest.ini                # Test configuration

Data & Models:
├── models/                    # Trained models
│   ├── scaler.pkl
│   ├── rf_model.pkl
│   ├── svm_model.pkl
│   ├── knn_model.pkl
│   └── nn_model.h5
├── SchizophreniaData.csv     # Training data
└── logs/                     # Application logs
```

## 🔍 Documentation by Audience

### For End Users
1. [QUICKSTART.md](QUICKSTART.md) - Setup and first use
2. [README.md](README.md) - Features and usage
3. Web interface at `http://localhost:5000`

### For Developers
1. [CONTRIBUTING.md](CONTRIBUTING.md) - How to contribute
2. [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API reference
3. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Architecture
4. Code comments in source files

### For DevOps/Admins
1. [DEPLOYMENT.md](DEPLOYMENT.md) - Deployment guide
2. [README.md](README.md) - System requirements
3. [QUICKSTART.md](QUICKSTART.md) - Installation

### For Project Managers
1. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Overview
2. [CHANGELOG.md](CHANGELOG.md) - Version history
3. [README.md](README.md) - Features and capabilities

## 🛠️ Technical Documentation

### API Endpoints
- `GET /` - Home page
- `GET /detection` - Detection form
- `POST /detection` - Submit prediction
- `GET /about` - About page
- `GET /history` - Prediction history
- `POST /api/predict` - API prediction
- `POST /api/compare` - Compare models

See [API_DOCUMENTATION.md](API_DOCUMENTATION.md) for details.

### Models
- **Random Forest** - Ensemble learning (Recommended)
- **SVM** - Support Vector Machine
- **KNN** - K-Nearest Neighbors
- **Neural Network** - Deep learning

See [README.md](README.md) for model details.

### Input Features
- Age (0-120)
- Gender (0=Male, 1=Female)
- Marital Status (0=Single, 1=Married)
- Fatigue (0-10)
- Slowing (0-10)
- Pain (0-10)
- Hygiene (0-10)
- Movement (0-10)

See [README.md](README.md) for feature descriptions.

## 📊 Version Information

- **Current Version**: 2.0.0
- **Release Date**: March 11, 2024
- **Status**: Production Ready
- **Python**: 3.8+
- **License**: MIT

See [CHANGELOG.md](CHANGELOG.md) for version history.

## 🔗 External Resources

### Dependencies
- [Flask Documentation](https://flask.palletsprojects.com/)
- [TensorFlow Documentation](https://www.tensorflow.org/api_docs)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)

### Deployment Platforms
- [Heroku](https://www.heroku.com/)
- [AWS](https://aws.amazon.com/)
- [Google Cloud](https://cloud.google.com/)
- [Azure](https://azure.microsoft.com/)

## ⚠️ Important Notes

### Medical Disclaimer
This tool is for educational purposes only. It should NOT be used for medical diagnosis. Always consult qualified healthcare professionals.

### Data Privacy
- No permanent storage of patient data
- Session-based tracking only
- Review privacy considerations before production use

### Security
- Change SECRET_KEY in production
- Use HTTPS/SSL
- Implement rate limiting
- Review security section in [DEPLOYMENT.md](DEPLOYMENT.md)

## 🆘 Getting Help

### Documentation
1. Check this index for relevant documentation
2. Search within specific documentation files
3. Review code comments

### Issues
1. Check "Common Issues" in [QUICKSTART.md](QUICKSTART.md)
2. Review "Troubleshooting" in [DEPLOYMENT.md](DEPLOYMENT.md)
3. Open a GitHub issue

### Contributing
1. Read [CONTRIBUTING.md](CONTRIBUTING.md)
2. Check existing issues and PRs
3. Follow contribution guidelines

## 📝 Documentation Maintenance

### Updating Documentation
- Keep documentation in sync with code
- Update CHANGELOG.md for each release
- Review and update examples
- Check for broken links

### Documentation Standards
- Clear and concise writing
- Code examples for complex topics
- Screenshots for UI features
- Version-specific information

## 🎓 Learning Path

### Beginner
1. [QUICKSTART.md](QUICKSTART.md) - Get started
2. [README.md](README.md) - Learn features
3. Use web interface

### Intermediate
1. [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API usage
2. [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) - Architecture
3. Integrate with your application

### Advanced
1. [CONTRIBUTING.md](CONTRIBUTING.md) - Contribute
2. [DEPLOYMENT.md](DEPLOYMENT.md) - Deploy
3. Extend functionality

## 📞 Contact & Support

- **Issues**: GitHub Issues
- **Documentation**: This repository
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

---

**Last Updated**: March 11, 2024  
**Version**: 2.0.0  
**Maintained by**: Project Team

---

Thank you for using the Schizophrenia Detection System! 🚀

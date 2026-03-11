# Changelog

All notable changes to the Schizophrenia Detection System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2024-03-11

### Added
- **Multiple ML Models**: Support for Random Forest, SVM, KNN, and Neural Network
- **Model Comparison**: Compare predictions across all models simultaneously
- **REST API**: Two new endpoints (`/api/predict` and `/api/compare`)
- **Confidence Scores**: Detailed probability distributions for predictions
- **Input Validation**: Comprehensive validation with helpful error messages
- **Prediction History**: Track and review past predictions during session
- **Logging System**: Complete logging of predictions and system events
- **Modern UI**: Completely redesigned responsive interface
- **Interactive Forms**: Range sliders for symptom assessment
- **About Page**: Comprehensive information about the system
- **History Page**: View past predictions
- **Error Pages**: Custom 404 and 500 error pages
- **Configuration Management**: Centralized config with environment variables
- **Testing Suite**: Comprehensive unit tests for models and API
- **Documentation**: Complete API documentation and deployment guide
- **Security Features**: Input sanitization and validation
- **Feature Ranges**: Defined valid ranges for all input features
- **Recommendations**: Detailed recommendations based on predictions
- **Model Selection**: Users can choose which model to use
- **Batch Scripts**: Easy run scripts for Windows and Linux

### Changed
- **Complete UI Overhaul**: Modern, responsive design with better UX
- **Enhanced Models**: Improved model training with cross-validation
- **Better Error Handling**: More informative error messages
- **Improved Logging**: Structured logging with timestamps
- **Updated Dependencies**: Latest versions of Flask, TensorFlow, scikit-learn
- **Code Structure**: Better organized with separate config file
- **Model Management**: Centralized ModelManager class
- **Training Script**: Enhanced with evaluation metrics and feature importance

### Improved
- **Performance**: Optimized model loading and prediction
- **Accessibility**: Better form labels and ARIA attributes
- **Mobile Support**: Fully responsive design
- **Code Quality**: Better documentation and type hints
- **Test Coverage**: Comprehensive test suite
- **Deployment**: Production-ready with Gunicorn support

### Fixed
- Model loading errors
- Input validation issues
- Session management
- Error handling in API endpoints

### Security
- Added input validation
- Implemented CSRF protection setup
- Sanitized user inputs
- Secure session configuration

## [1.0.0] - 2024-01-01

### Added
- Initial release
- Basic Flask application
- Single model prediction (Neural Network)
- Simple web interface
- Basic form for data input
- Model training script

### Features
- Schizophrenia detection using neural network
- Web-based interface
- Basic prediction functionality

---

## Upcoming Features

### [2.1.0] - Planned
- [ ] User authentication system
- [ ] Database integration for persistent storage
- [ ] Advanced data visualization
- [ ] Export predictions to PDF/CSV
- [ ] Email notifications
- [ ] Admin dashboard

### [3.0.0] - Future
- [ ] Mobile application
- [ ] Real-time monitoring
- [ ] Integration with EHR systems
- [ ] Multi-language support
- [ ] Advanced analytics
- [ ] Machine learning model retraining interface

---

## Version History

- **2.0.0** (2024-03-11): Major update with multiple models, API, and modern UI
- **1.0.0** (2024-01-01): Initial release with basic functionality

---

For detailed information about each release, see the [GitHub Releases](https://github.com/your-repo/releases) page.

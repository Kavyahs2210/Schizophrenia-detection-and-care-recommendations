# Contributing to Schizophrenia Detection System

Thank you for your interest in contributing! This document provides guidelines for contributing to the project.

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment
- Remember this is a mental health-related project - be sensitive

## How to Contribute

### Reporting Bugs

1. Check if the bug has already been reported in Issues
2. If not, create a new issue with:
   - Clear title and description
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version)
   - Screenshots if applicable

### Suggesting Enhancements

1. Check if the enhancement has been suggested
2. Create an issue describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Why this enhancement would be useful

### Pull Requests

1. Fork the repository
2. Create a feature branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. Make your changes following our coding standards

4. Add tests for new features

5. Update documentation as needed

6. Commit with clear messages:
   ```bash
   git commit -m "Add feature: description"
   ```

7. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```

8. Create a Pull Request with:
   - Clear description of changes
   - Reference to related issues
   - Screenshots for UI changes

## Development Setup

1. Clone your fork:
```bash
git clone https://github.com/your-username/schizophrenia-detection.git
cd schizophrenia-detection
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run tests:
```bash
pytest
```

## Coding Standards

### Python Style

- Follow PEP 8
- Use meaningful variable names
- Add docstrings to functions and classes
- Keep functions focused and small
- Maximum line length: 100 characters

Example:
```python
def predict_schizophrenia(features, model_type='rf'):
    """
    Make a prediction using specified model.
    
    Args:
        features (list): Patient feature values
        model_type (str): Model to use (rf, svm, knn, nn)
    
    Returns:
        dict: Prediction results with class and confidence
    """
    # Implementation
    pass
```

### HTML/CSS

- Use semantic HTML5 elements
- Follow BEM naming convention for CSS
- Ensure accessibility (ARIA labels, alt text)
- Mobile-first responsive design

### JavaScript

- Use ES6+ features
- Add comments for complex logic
- Handle errors gracefully
- Validate user input

## Testing

### Writing Tests

- Write tests for new features
- Maintain test coverage above 80%
- Use descriptive test names
- Test edge cases

Example:
```python
def test_valid_prediction():
    """Test prediction with valid input"""
    features = [35, 0, 1, 5.5, 3.2, 2.1, 1.5, 2.8]
    result = model_manager.predict(features, 'rf')
    assert 'class' in result
    assert result['class'] in [0, 1]
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_models.py

# Run specific test
pytest tests/test_models.py::TestModelManager::test_predict_rf
```

## Documentation

- Update README.md for new features
- Add API documentation for new endpoints
- Include code comments for complex logic
- Update CHANGELOG.md

## Commit Messages

Format:
```
<type>: <subject>

<body>

<footer>
```

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

Example:
```
feat: Add model comparison endpoint

- Implement /api/compare endpoint
- Return predictions from all models
- Add tests for comparison functionality

Closes #123
```

## Project Structure

```
schizophrenia-detection/
├── app.py              # Main application
├── models.py           # Model management
├── config.py           # Configuration
├── static/             # CSS, JS, images
├── templates/          # HTML templates
├── tests/              # Test files
├── models/             # Trained models
└── logs/               # Application logs
```

## Areas for Contribution

### High Priority
- [ ] Add more ML models (XGBoost, LightGBM)
- [ ] Implement user authentication
- [ ] Add database support
- [ ] Create mobile app
- [ ] Improve test coverage

### Medium Priority
- [ ] Add data visualization
- [ ] Implement caching
- [ ] Add internationalization
- [ ] Create admin dashboard
- [ ] Add export functionality

### Low Priority
- [ ] Dark mode theme
- [ ] Email notifications
- [ ] Social media integration
- [ ] Advanced analytics

## Questions?

- Open an issue for questions
- Check existing documentation
- Review closed issues and PRs

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for contributing to mental health awareness and technology!

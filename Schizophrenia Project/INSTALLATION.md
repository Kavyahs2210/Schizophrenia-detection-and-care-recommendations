# Installation Guide

Complete step-by-step installation guide for the Schizophrenia Detection System.

## System Requirements

### Minimum Requirements
- **OS**: Windows 10/11, Linux (Ubuntu 18.04+), macOS 10.14+
- **Python**: 3.8 or higher
- **RAM**: 4 GB minimum, 8 GB recommended
- **Disk Space**: 2 GB free space
- **Internet**: Required for initial setup

### Recommended Requirements
- **Python**: 3.9 or 3.10
- **RAM**: 8 GB or more
- **CPU**: Multi-core processor
- **Disk Space**: 5 GB free space

## Pre-Installation Checklist

- [ ] Python 3.8+ installed
- [ ] pip package manager available
- [ ] Virtual environment tool (venv)
- [ ] Git (optional, for cloning)
- [ ] Internet connection
- [ ] Administrator/sudo access (if needed)

## Installation Methods

### Method 1: Automated Installation (Recommended)

#### Windows
1. Open Command Prompt or PowerShell
2. Navigate to project directory
3. Run the automated script:
```cmd
run.bat
```

#### Linux/Mac
1. Open Terminal
2. Navigate to project directory
3. Make script executable and run:
```bash
chmod +x run.sh
./run.sh
```

The script will:
- Create virtual environment
- Install dependencies
- Create necessary directories
- Check for trained models
- Start the application

### Method 2: Manual Installation

#### Step 1: Download/Clone Project
```bash
# If using Git
git clone <repository-url>
cd schizophrenia-detection

# Or download and extract ZIP file
```

#### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Or use python3 on Linux/Mac
python3 -m venv venv
```

#### Step 3: Activate Virtual Environment

**Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell):**
```powershell
venv\Scripts\Activate.ps1
```

**Linux/Mac:**
```bash
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### Step 4: Upgrade pip (Recommended)
```bash
python -m pip install --upgrade pip
```

#### Step 5: Install Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- Flask 3.0.0
- TensorFlow 2.15.0
- Scikit-learn 1.3.2
- NumPy 1.24.3
- Pandas 2.1.4
- And other dependencies

**Note**: TensorFlow installation may take several minutes.

#### Step 6: Create Required Directories
```bash
# Windows
mkdir logs

# Linux/Mac
mkdir -p logs
```

The `models` directory should already exist with trained models.

#### Step 7: Verify Installation
```bash
python verify_setup.py
```

This will check:
- Python version
- Installed dependencies
- Required directories
- Core files
- Trained models
- Configuration
- Module imports

#### Step 8: Train Models (If Needed)

If models don't exist or you want to retrain:
```bash
python train_all_models.py
```

This will:
- Load the dataset
- Preprocess data
- Train all 4 models
- Save models to `models/` directory
- Display performance metrics

**Note**: Training may take 5-15 minutes depending on your hardware.

#### Step 9: Configure Environment (Optional)
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your settings
# Windows: notepad .env
# Linux/Mac: nano .env
```

Set your configuration:
```env
SECRET_KEY=your-secret-key-here
FLASK_ENV=development
FLASK_DEBUG=True
```

#### Step 10: Run Application
```bash
python app.py
```

You should see:
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
```

#### Step 11: Access Application

Open your browser and navigate to:
```
http://localhost:5000
```

## Verification Steps

### 1. Check Python Version
```bash
python --version
# Should show Python 3.8 or higher
```

### 2. Check pip
```bash
pip --version
# Should show pip version
```

### 3. Verify Virtual Environment
```bash
# Should show (venv) in prompt
which python  # Linux/Mac
where python  # Windows
# Should point to venv directory
```

### 4. Test Imports
```bash
python -c "import flask; print(flask.__version__)"
python -c "import tensorflow; print(tensorflow.__version__)"
python -c "import sklearn; print(sklearn.__version__)"
```

### 5. Run Verification Script
```bash
python verify_setup.py
```

All checks should pass.

### 6. Run Tests
```bash
pytest
```

All tests should pass.

## Troubleshooting

### Issue: Python not found
**Solution**: 
- Install Python from [python.org](https://www.python.org/downloads/)
- Add Python to PATH during installation
- Restart terminal after installation

### Issue: pip not found
**Solution**:
```bash
python -m ensurepip --upgrade
```

### Issue: Virtual environment activation fails (Windows PowerShell)
**Solution**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: TensorFlow installation fails
**Solutions**:
1. Update pip: `python -m pip install --upgrade pip`
2. Install specific version: `pip install tensorflow==2.15.0`
3. On Windows, ensure Visual C++ Redistributable is installed
4. On Mac M1/M2, use: `pip install tensorflow-macos`

### Issue: Permission denied (Linux/Mac)
**Solution**:
```bash
# Don't use sudo with pip in virtual environment
# If needed for system packages:
sudo apt-get install python3-dev python3-pip
```

### Issue: Models not found
**Solution**:
```bash
python train_all_models.py
```

### Issue: Port 5000 already in use
**Solution**:

**Windows:**
```cmd
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

**Linux/Mac:**
```bash
lsof -ti:5000 | xargs kill -9
```

Or change port in `app.py`:
```python
app.run(debug=True, port=5001)
```

### Issue: Module import errors
**Solution**:
1. Ensure virtual environment is activated
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Check Python version compatibility

### Issue: Dataset not found
**Solution**:
- Ensure `SchizophreniaData.csv` is in project root
- Check file name spelling
- Verify file is not corrupted

## Platform-Specific Notes

### Windows
- Use Command Prompt or PowerShell
- Backslashes in paths: `venv\Scripts\activate`
- May need to allow Python through firewall
- Visual C++ Redistributable required for TensorFlow

### Linux
- May need to install python3-venv: `sudo apt-get install python3-venv`
- Use forward slashes: `venv/bin/activate`
- May need build tools: `sudo apt-get install build-essential`

### macOS
- Use Terminal
- May need Xcode Command Line Tools: `xcode-select --install`
- On M1/M2, use tensorflow-macos
- Use `python3` instead of `python`

## Post-Installation

### 1. Test Web Interface
- Navigate to `http://localhost:5000`
- Click through all pages
- Submit a test prediction
- Check prediction history

### 2. Test API
```bash
curl -X POST http://localhost:5000/api/predict \
  -H "Content-Type: application/json" \
  -d '{"features": {"Age": 35, "Gender": 0, "Marital_Status": 1, "Fatigue": 5.5, "Slowing": 3.2, "Pain": 2.1, "Hygiene": 1.5, "Movement": 2.8}, "model_type": "rf"}'
```

### 3. Review Logs
```bash
# Check application logs
cat logs/app.log  # Linux/Mac
type logs\app.log  # Windows
```

### 4. Run Tests
```bash
pytest -v
```

## Updating

### Update Dependencies
```bash
pip install --upgrade -r requirements.txt
```

### Update Application
```bash
git pull origin main  # If using Git
# Or download latest version
```

### Retrain Models
```bash
python train_all_models.py
```

## Uninstallation

### Remove Virtual Environment
```bash
# Deactivate first
deactivate

# Remove directory
rm -rf venv  # Linux/Mac
rmdir /s venv  # Windows
```

### Remove Application
```bash
# Remove entire directory
rm -rf schizophrenia-detection  # Linux/Mac
rmdir /s schizophrenia-detection  # Windows
```

## Next Steps

After successful installation:

1. **Read Documentation**
   - [QUICKSTART.md](QUICKSTART.md) - Quick start guide
   - [README.md](README.md) - Complete documentation
   - [API_DOCUMENTATION.md](API_DOCUMENTATION.md) - API reference

2. **Explore Features**
   - Try different models
   - Test API endpoints
   - Review prediction history
   - Check about page

3. **Development**
   - Read [CONTRIBUTING.md](CONTRIBUTING.md)
   - Run tests: `pytest`
   - Review code structure

4. **Deployment**
   - Read [DEPLOYMENT.md](DEPLOYMENT.md)
   - Configure for production
   - Deploy to server

## Support

### Documentation
- Check [INDEX.md](INDEX.md) for all documentation
- Review specific guides for your needs
- Read code comments

### Common Issues
- See troubleshooting section above
- Check [QUICKSTART.md](QUICKSTART.md)
- Review logs in `logs/app.log`

### Getting Help
- Open GitHub issue
- Check existing issues
- Review documentation

## Security Notes

### Development
- Default SECRET_KEY is for development only
- Debug mode should be disabled in production
- Review security checklist before deployment

### Production
- Set strong SECRET_KEY
- Disable debug mode
- Use HTTPS/SSL
- Implement rate limiting
- Review [DEPLOYMENT.md](DEPLOYMENT.md)

## Performance Tips

### Development
- Use development server for testing
- Enable debug mode for detailed errors
- Use small dataset for quick testing

### Production
- Use Gunicorn or similar WSGI server
- Disable debug mode
- Use production-grade database
- Implement caching
- Use CDN for static files

## Maintenance

### Regular Tasks
- Update dependencies monthly
- Review logs weekly
- Backup models regularly
- Monitor performance
- Update documentation

### Monitoring
- Check logs: `logs/app.log`
- Monitor disk space
- Track prediction accuracy
- Review error rates

---

## Installation Complete! 🎉

You should now have:
- ✅ Virtual environment set up
- ✅ All dependencies installed
- ✅ Required directories created
- ✅ Models trained and ready
- ✅ Application running
- ✅ Tests passing

**Access your application at**: `http://localhost:5000`

For next steps, see [QUICKSTART.md](QUICKSTART.md) or [README.md](README.md).

---

**Need help?** Check the troubleshooting section or open an issue on GitHub.

**Happy coding!** 🚀

# Deployment Guide

Complete guide for deploying the Schizophrenia Detection System to production.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Local Development](#local-development)
3. [Production Deployment](#production-deployment)
4. [Docker Deployment](#docker-deployment)
5. [Cloud Deployment](#cloud-deployment)
6. [Security Considerations](#security-considerations)
7. [Monitoring & Maintenance](#monitoring--maintenance)

## Prerequisites

- Python 3.8+
- pip package manager
- Virtual environment tool
- Git
- (Optional) Docker
- (Optional) Cloud account (AWS, GCP, Azure, Heroku)

## Local Development

### Setup

1. Clone and setup:
```bash
git clone <repository-url>
cd schizophrenia-detection
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env with your settings
```

3. Run development server:
```bash
python app.py
```

Access at: `http://localhost:5000`

## Production Deployment

### Using Gunicorn

1. Install Gunicorn:
```bash
pip install gunicorn
```

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

Options:
- `-w 4`: 4 worker processes
- `-b 0.0.0.0:5000`: Bind to all interfaces on port 5000
- `--timeout 120`: Request timeout (seconds)
- `--access-logfile logs/access.log`: Access logs
- `--error-logfile logs/error.log`: Error logs

3. Create systemd service (Linux):

Create `/etc/systemd/system/schizophrenia-detection.service`:

```ini
[Unit]
Description=Schizophrenia Detection System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/schizophrenia-detection
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 0.0.0.0:5000 app:app

[Install]
WantedBy=multi-user.target
```

Enable and start:
```bash
sudo systemctl enable schizophrenia-detection
sudo systemctl start schizophrenia-detection
sudo systemctl status schizophrenia-detection
```

### Nginx Reverse Proxy

1. Install Nginx:
```bash
sudo apt install nginx
```

2. Create Nginx config `/etc/nginx/sites-available/schizophrenia-detection`:

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/schizophrenia-detection/static;
        expires 30d;
    }
}
```

3. Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/schizophrenia-detection /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### SSL with Let's Encrypt

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d your-domain.com
```

## Docker Deployment

### Dockerfile

Create `Dockerfile`:

```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Create logs directory
RUN mkdir -p logs

# Expose port
EXPOSE 5000

# Run with gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--timeout", "120", "app:app"]
```

### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    volumes:
      - ./logs:/app/logs
      - ./models:/app/models
    environment:
      - SECRET_KEY=${SECRET_KEY}
      - FLASK_ENV=production
    restart: unless-stopped
```

### Build and Run

```bash
# Build image
docker build -t schizophrenia-detection .

# Run container
docker run -d -p 5000:5000 --name schizo-app schizophrenia-detection

# Or use docker-compose
docker-compose up -d
```

## Cloud Deployment

### Heroku

1. Create `Procfile`:
```
web: gunicorn app:app
```

2. Create `runtime.txt`:
```
python-3.9.16
```

3. Deploy:
```bash
heroku login
heroku create your-app-name
git push heroku main
heroku open
```

### AWS EC2

1. Launch EC2 instance (Ubuntu 20.04)
2. SSH into instance
3. Install dependencies:
```bash
sudo apt update
sudo apt install python3-pip python3-venv nginx
```

4. Clone and setup application
5. Configure Nginx and systemd (see above)
6. Configure security groups (allow ports 80, 443)

### Google Cloud Platform

1. Create `app.yaml`:
```yaml
runtime: python39

instance_class: F2

automatic_scaling:
  target_cpu_utilization: 0.65
  min_instances: 1
  max_instances: 10

handlers:
- url: /static
  static_dir: static

- url: /.*
  script: auto
```

2. Deploy:
```bash
gcloud app deploy
```

### Azure App Service

1. Create Web App
2. Configure deployment:
```bash
az webapp up --name your-app-name --resource-group your-rg
```

## Security Considerations

### Environment Variables

Never commit sensitive data. Use environment variables:

```bash
# .env (never commit this)
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
API_KEY=your-api-key
```

### Security Headers

Add to Nginx config:
```nginx
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-XSS-Protection "1; mode=block" always;
add_header Strict-Transport-Security "max-age=31536000" always;
```

### Rate Limiting

Install Flask-Limiter:
```bash
pip install Flask-Limiter
```

Add to `app.py`:
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["100 per minute"]
)
```

### CORS (if needed)

```bash
pip install flask-cors
```

```python
from flask_cors import CORS
CORS(app, resources={r"/api/*": {"origins": "https://your-domain.com"}})
```

## Monitoring & Maintenance

### Logging

Logs are in `logs/app.log`. Monitor with:
```bash
tail -f logs/app.log
```

### Health Check Endpoint

Add to `app.py`:
```python
@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200
```

### Monitoring Tools

- **Uptime monitoring**: UptimeRobot, Pingdom
- **Application monitoring**: New Relic, DataDog
- **Error tracking**: Sentry

### Backup

Backup models and logs regularly:
```bash
tar -czf backup-$(date +%Y%m%d).tar.gz models/ logs/
```

### Updates

1. Pull latest code
2. Activate virtual environment
3. Update dependencies: `pip install -r requirements.txt`
4. Restart service: `sudo systemctl restart schizophrenia-detection`

## Performance Optimization

### Caching

Install Flask-Caching:
```bash
pip install Flask-Caching
```

### Load Balancing

Use multiple Gunicorn workers:
```bash
gunicorn -w $(nproc) -b 0.0.0.0:5000 app:app
```

### Database (if added)

Use connection pooling and indexing for better performance.

## Troubleshooting

### Check logs
```bash
tail -f logs/app.log
sudo journalctl -u schizophrenia-detection -f
```

### Test API
```bash
curl http://localhost:5000/health
```

### Restart services
```bash
sudo systemctl restart schizophrenia-detection
sudo systemctl restart nginx
```

## Checklist

Before deploying to production:

- [ ] Set strong SECRET_KEY
- [ ] Configure environment variables
- [ ] Enable HTTPS/SSL
- [ ] Set up monitoring
- [ ] Configure backups
- [ ] Test all endpoints
- [ ] Set up error tracking
- [ ] Configure rate limiting
- [ ] Review security headers
- [ ] Test with production data
- [ ] Document deployment process
- [ ] Set up CI/CD (optional)

---

For questions or issues, consult the main README or open a GitHub issue.

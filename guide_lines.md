# Django Full-Stack Project Development Rules
Last Updated: 2025-03-07 15:33:31
Author: punitDT

## Initial Steps

- create venv
- create change_log.md and write every change you make in project
- select python interpreter 
- run all commands in activated venv

## Project Structure
```
project_name/
├── manage.py
├── requirements/
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── config/
│   ├── __init__.py
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── utils.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── forms.py
│   │   └── tests.py
│   └── api/
│       ├── __init__.py
│       ├── views.py
│       ├── urls.py
│       └── serializers.py
├── templates/
│   ├── base.html
│   ├── components/
│   └── pages/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
├── docs/
└── scripts/
```

## 1. Django Project Rules

### 1.1 Django Version and Dependencies
- Use Django 5.x (LTS version preferred)
- Pin all requirements versions
- Separate requirements by environment
- Use virtual environment

### 1.2 Settings Configuration
```python
# Example settings structure
config/settings/
├── base.py      # Shared settings
├── local.py     # Development settings
└── production.py # Production settings
```

### 1.3 Environment Variables
- Use python-dotenv for environment variables
- Never commit .env files
- Template structure:
```
# .env.example
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=postgresql://user:pass@localhost:5432/dbname
```

## 2. Django Apps Organization

### 2.1 App Structure
Each app should follow:
```
app_name/
├── __init__.py
├── admin.py      # Admin configurations
├── apps.py       # App configuration
├── models.py     # Database models
├── serializers.py # DRF serializers (if API)
├── services.py   # Business logic
├── urls.py       # URL patterns
├── views.py      # View logic
└── tests/
    ├── __init__.py
    ├── test_models.py
    ├── test_views.py
    └── test_services.py
```

### 2.2 App Naming Conventions
- Use lowercase
- Use singular form
- Be descriptive (e.g., 'authentication' not 'auth')

## 3. Django Models

### 3.1 Model Definition Rules
```python
# Example model structure
from django.db import models
from django.utils.translation import gettext_lazy as _

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class YourModel(BaseModel):
    name = models.CharField(_("Name"), max_length=100)
    
    class Meta:
        verbose_name = _("Your Model")
        verbose_name_plural = _("Your Models")
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
```

### 3.2 Model Fields
- Use verbose_name for all fields
- Set appropriate field sizes
- Use choices for fixed options
- Include help_text where needed

## 4. Views and Templates

### 4.1 View Rules
- Use Class-Based Views when possible
- Implement proper permission mixins
- Keep business logic in services.py

### 4.2 Template Structure
```
templates/
├── base.html
├── components/
│   ├── navbar.html
│   ├── footer.html
│   └── forms/
├── pages/
│   ├── home.html
│   └── dashboard.html
└── emails/
```

## 5. Forms and Validation

### 5.1 Form Structure
```python
# Example form structure
from django import forms

class YourForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = ['field1', 'field2']
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control'})
        }
```

### 5.2 Form Validation
- Use clean_fieldname methods
- Implement form-wide validation in clean()
- Add error messages to fields

## 6. API Development (DRF)

### 6.1 API Structure
```python
# views.py
from rest_framework import viewsets

class YourModelViewSet(viewsets.ModelViewSet):
    queryset = YourModel.objects.all()
    serializer_class = YourModelSerializer
    permission_classes = [IsAuthenticated]
```

### 6.2 API Versioning
- Use URL versioning
- Version format: v1, v2, etc.
- Maintain backwards compatibility

## 7. Testing

### 7.1 Test Structure
```python
# tests/test_views.py
from django.test import TestCase
from django.urls import reverse

class YourViewTests(TestCase):
    def setUp(self):
        # Setup test data
        pass

    def test_view_response(self):
        url = reverse('view-name')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
```

### 7.2 Testing Rules
- Minimum 80% coverage
- Test all models and views
- Use factories for test data
- Mock external services

## 8. Static Files

### 8.1 Static Files Organization
```
static/
├── css/
│   ├── base.css
│   └── components/
├── js/
│   ├── main.js
│   └── modules/
└── images/
```

### 8.2 Static Files Rules
- Use django-compressor
- Implement caching
- Optimize assets
- Use CDN in production

## 9. Security

### 9.1 Security Checklist
- Enable CSRF protection
- Set secure cookie settings
- Configure CORS properly
- Use HTTPS in production
- Implement rate limiting

### 9.2 Authentication
- Use django-allauth
- Implement 2FA where needed
- Use strong password validation

## 10. Deployment

### 10.1 Deployment Checklist
```python
# settings/production.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

### 10.2 Production Setup
- Use gunicorn + nginx
- Configure PostgreSQL
- Setup Redis for caching
- Enable logging

## 11. Code Style

### 11.1 Python Style
- Follow PEP 8
- Use Black formatter
- Maximum line length: 88
- Use isort for imports

### 11.2 Documentation
- Document all models
- Add docstrings to views
- Comment complex logic
- Maintain README.md

## 12. Version Control

### 12.1 Git Workflow
- Feature branch naming: `feature/feature-name`
- Bugfix branch naming: `bugfix/issue-description`
- Release branch naming: `release/v1.0.0`

### 12.2 Commit Messages
```
feat(users): add email verification
fix(auth): resolve login redirect issue
docs(api): update API documentation
```

## 13. Maintenance

### 13.1 Regular Tasks
- Update dependencies monthly
- Run security checks
- Monitor error logs
- Backup database regularly

### 13.2 Performance
- Use debug toolbar in development
- Monitor query performance
- Implement caching strategy
- Use Django ORM efficiently

---

# research_exp_project

This project is a Django-based application for managing research experiments, researchers, samples, and measurements.

## Structure

- `manage.py` - Django management script.
- `research_exp_app/` - Main Django app containing:
  - `models.py` - Database models for experiments, researchers, samples, and measurements.
  - `modular_functions/data/` - Utility scripts for inserting and managing data.
  - `views.py`, `urls.py`, `admin.py` - Standard Django app files.
- `research_experiment/` - Django project settings and configuration files.

## Getting Started

1. Install dependencies:
   ```bash
   pip install django
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Start the development server:
   ```bash
   python manage.py runserver
   ```


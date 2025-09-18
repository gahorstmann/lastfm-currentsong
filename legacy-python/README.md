# Legacy Python Flask Application

This directory contains the original Python Flask application that was used to generate SVG widgets showing the current Last.fm song.

## What was here

- **Flask REST API** with endpoints:
  - `/current/<user_id>` - Returns SVG widget
  - `/currentjson/<user_id>` - Returns JSON data
  - `/health` - Health check endpoint

- **Features**:
  - SVG generation with custom themes (light, dark, nord, dracula)
  - Multiple styles (default, spotify)
  - Custom reload intervals
  - Jinja2 templates for SVG rendering

## Migration to JAMStack

This application has been refactored to use modern JAMStack architecture:

- **Before**: Python Flask app + SVG generation
- **After**: React frontend + Cloudflare Pages Functions

The new implementation provides:
- Better performance with static hosting
- Modern React UI instead of SVG widgets
- Serverless functions for API calls
- Easier deployment and scaling

## Files archived

- `app/` - Flask application code
- `test/` - Python unit tests
- `main.py` - Flask application entry point
- `Pipfile` & `Pipfile.lock` - Python dependencies
- `docker-compose.yaml` - Docker configuration

These files are preserved for reference but are no longer actively used.
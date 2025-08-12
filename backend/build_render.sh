#!/bin/bash

# Render Deployment Build Script for Knowledge-ledger Backend
# This script is specifically optimized for Render's deployment environment

set -e  # Exit on any error

echo "🚀 Starting Render Production Build Process..."

# Render automatically sets these environment variables
echo "🔧 Render Environment Variables:"
echo "   PORT: $PORT"
echo "   RENDER: $RENDER"
echo "   RENDER_SERVICE_NAME: $RENDER_SERVICE_NAME"
echo "   RENDER_SERVICE_TYPE: $RENDER_SERVICE_TYPE"

echo "📦 Installing Production Dependencies..."
pip install -r requirements.txt

echo "🗄️  Running Database Migrations..."
python manage.py migrate --no-input

echo "📁 Collecting Static Files for Render..."
python manage.py collectstatic --no-input --clear

echo "🔍 Running Production Security Checks..."
python manage.py check --deploy

echo "🧹 Cleaning up temporary files..."
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -delete

echo "📊 Render Build Summary:"
echo "   ✅ Dependencies installed"
echo "   ✅ Database migrated"
echo "   ✅ Static files collected"
echo "   ✅ Security checks passed"
echo "   ✅ Cache cleared"

echo "🎉 Render Build Complete!"
echo "🚀 Your Django app is ready for Render deployment!"

# Optional: Create superuser if environment variable is set
if [[ $CREATE_SUPERUSER == "True" ]]; then
    echo "👤 Creating superuser..."
    python manage.py createsuperuser --no-input
    echo "✅ Superuser created successfully!"
fi

echo "💡 Render Deployment Notes:"
echo "   1. Static files are collected in 'staticfiles' directory"
echo "   2. Database migrations are automatically applied"
echo "   3. Gunicorn will start on port $PORT"
echo "   4. Environment variables are set via Render dashboard"
echo "   5. SSL is automatically handled by Render"

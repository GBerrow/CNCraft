#!/usr/bin/env bash
# Render build script for CNCraft Django application

set -o errexit  # Exit on any error

echo "🔧 Starting CNCraft build process..."

# Install Python dependencies
echo "📦 Installing Python packages..."
pip install -r requirements.txt

# Collect static files
echo "📂 Collecting static files..."
python manage.py collectstatic --no-input

# Run database migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Populate CNC products (only if database is empty)
echo "🛠️ Populating CNC products..."
python manage.py populate_cnc_products

echo "✅ Build completed successfully!"

#!/bin/bash

# Smart CV Evaluator - Docker startup script for Linux/Mac

echo "🐳 Starting Smart CV Evaluator with Docker..."
echo ""

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "🔨 Building Docker image..."
docker build -t smart-cv-evaluator .

if [ $? -ne 0 ]; then
    echo "❌ Failed to build Docker image."
    exit 1
fi

echo ""
echo "🚀 Starting container..."
echo "The application will be available at: http://localhost:8501"
echo ""

# Start the container
docker run -p 8501:8501 \
  -v "$(pwd)/uploads:/app/uploads" \
  -v "$(pwd)/temp:/app/temp" \
  smart-cv-evaluator

#!/bin/bash

# Smart CV Evaluator - Linux/Mac startup script

echo "🚀 Starting Smart CV Evaluator..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.10+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

echo "📦 Installing dependencies..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install dependencies."
    exit 1
fi

echo ""
echo "🎯 Starting Streamlit application..."
echo "The application will be available at: http://localhost:8501"
echo ""

# Start the application
streamlit run app.py

@echo off
echo Starting Smart CV Evaluator with Docker...
echo.
echo Building Docker image...
docker build -t smart-cv-evaluator .
echo.
echo Starting container...
docker run -p 8501:8501 -v "%cd%\uploads:/app/uploads" -v "%cd%\temp:/app/temp" smart-cv-evaluator
echo.
echo The application will be available at: http://localhost:8501
pause

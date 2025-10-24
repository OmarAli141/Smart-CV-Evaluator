@echo off
echo Starting Smart CV Evaluator...
echo.
echo Installing dependencies...
pip install -r requirements.txt
echo.
echo Starting Streamlit application...
echo The application will be available at: http://localhost:8501
echo.
streamlit run app.py
pause

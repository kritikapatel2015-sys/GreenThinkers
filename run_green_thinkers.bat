@echo off
REM ------------------------------
REM Green Thinkers Full Setup & Launch
REM ------------------------------

:: Navigate to script folder
cd /d %~dp0

:: Step 1: Create virtual environment if it doesn't exist
if not exist green_env (
    python -m venv green_env
)

:: Step 2: Activate virtual environment
call green_env\Scripts\activate

:: Step 3: Upgrade pip
python -m pip install --upgrade pip

:: Step 4: Install all dependencies
pip install streamlit torch torchvision timm pillow diffusers transformers matplotlib

:: Step 5: Run the Streamlit app
streamlit run green_thinkers.py

pause

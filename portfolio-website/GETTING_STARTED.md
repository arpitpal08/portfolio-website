# Getting Started with Your Portfolio Website

This guide will help you get your portfolio website up and running quickly.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Create a virtual environment** (recommended):
   ```
   python -m venv venv
   ```

2. **Activate the virtual environment**:
   - On Windows (PowerShell):
     ```
     .\venv\Scripts\Activate.ps1
     ```
   - On Windows (Command Prompt):
     ```
     venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

### On Windows

You have several options to run the application:

1. **Using PowerShell script** (recommended):
   ```
   .\run_app.ps1
   ```

2. **Using batch file**:
   ```
   run.bat
   ```

3. **Using Python directly**:
   ```
   python run.py
   ```

### On macOS/Linux

1. **Using shell script** (recommended):
   ```
   chmod +x run.sh
   ./run.sh
   ```

2. **Using Python directly**:
   ```
   python run.py
   ```

## Running Tests

### On Windows

1. **Using PowerShell script** (recommended):
   ```
   .\run_tests.ps1
   ```

2. **Using batch file**:
   ```
   run_tests.bat
   ```

3. **Using Python directly**:
   ```
   python test_app.py
   ```

### On macOS/Linux

1. **Using shell script** (recommended):
   ```
   chmod +x run_tests.sh
   ./run_tests.sh
   ```

2. **Using Python directly**:
   ```
   python test_app.py
   ```

## Accessing the Website

Once the application is running, you can access it by opening your web browser and navigating to:
```
http://127.0.0.1:5000/
```

## Directory Structure

- `app.py`: Main Flask application
- `run.py`: Script to run the application
- `test_app.py`: Tests for the application
- `requirements.txt`: Python dependencies
- `frontend/`: Frontend files (HTML, CSS, JS)
- `backend/`: Backend files (API, data models, services)
- `ai-chatbot/`: AI chatbot implementation

## Customizing the Website

1. **Update HTML templates** in `frontend/templates/`
2. **Modify CSS styles** in `frontend/static/css/`
3. **Update JavaScript** in `frontend/static/js/`
4. **Add your own images** to `frontend/static/images/`
5. **Customize chatbot responses** in `ai-chatbot/data/knowledge_base.json`

## Deployment

See the `README.md` file for detailed deployment instructions for various platforms:
- Heroku
- Google Cloud Platform
- AWS
- Netlify 
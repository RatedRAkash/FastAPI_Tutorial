# FastAPI Tutorial

### Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/RatedRAkash/FastAPI_Tutorial.git
```

### 2. Create and Activate Virtual Environment and install dependencies
```bash
python -m venv my_venv
source my_venv/bin/activate
pip install -r requirements.txt
```

### 3. To run in Development Mode
```bash
fastapi dev main.py
```

### 4. Start Uvicorn Server for Production
```bash
uvicorn main:app --reload
```

For Production run with Multiple Workers
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4 --reload
```
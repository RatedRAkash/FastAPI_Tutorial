FROM python:3.11-slim

# Set working directory
WORKDIR /web_app

# Install dependencies early to cache this layer
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code later (only triggers rebuild if code changed)
COPY . .

EXPOSE 9998

# as the WORKDIR is `/web_app/` folder... so the CMD, RUN & Other Commands are Run on that specific Folder
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "9998", "--workers", "4", "--reload"]
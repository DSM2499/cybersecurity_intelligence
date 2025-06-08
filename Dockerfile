# Use official Python 3.10 base image
FROM python:3.10-slim

#Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create and set the working directory
WORKDIR /app

# Install system dependencies (optional — for pdf, etc.)
RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev curl && rm -rf /var/lib/apt/lists/*


# Copy requirements.txt and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#Copy rest of the app
COPY . /app/

# Default command — run main.py
CMD ["python", "main.py"]
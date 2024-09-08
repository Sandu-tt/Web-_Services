# Use the official Python image from the Docker Hub
FROM python:3.8-slim
# # Use official Python image as base
# FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . .

# Expose port
EXPOSE 5005

# Run the application
CMD ["python", "app/app.py"]
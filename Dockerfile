# Use the official Python image with a specific version (e.g., 3.9)
FROM python:3.12-slim

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the FastAPI application
EXPOSE 8000

# Run the FastAPI app with Uvicorn through Gunicorn
# CMD ["gunicorn", "app:app", "-k", "uvicorn.workers.UvicornWorker", "--bind", "127.0.0.1:8000", "--workers", "4"]
# CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]
CMD ["python", "app.py"]
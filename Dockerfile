# Use lightweight official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install required Python packages
RUN pip install -r requirements.txt

# Copy project files into container
COPY . .

# Set Python module search path
ENV PYTHONPATH=/app

# Run automated tests when container starts
CMD ["python", "-m", "pytest"]
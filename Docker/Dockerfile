# Use an official Python image
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the application files
COPY app.py /app/

# Install dependencies
RUN pip install flask prometheus-client flask-prometheus-metrics

# Define the command to run the app
CMD ["python", "app.py"]

# Use an official Python image
FROM python:3.11-slim-buster

# Set the working directory
WORKDIR /app

# Copy the application files
COPY requirements.txt /app/
COPY app.py /app/


# Install dependencies
RUN pip install -r requirements.txt

# Define the command to run the app
CMD ["python", "app.py"]

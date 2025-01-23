# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory's contents into the container
COPY . /app

# Install required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["flask", "run"]

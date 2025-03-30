# Use the official Miniconda image as a base image
FROM continuumio/miniconda3:latest

# Set the working directory inside the container
WORKDIR /app

# Install build-essential for compiling
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a Conda environment with Python 3.8
RUN conda create --name myenv python=3.8

# Set Conda environment activation for subsequent RUN commands
SHELL ["conda", "run", "-n", "myenv", "/bin/bash", "-c"]

# Clone the repository
RUN git clone https://github.com/operator259/ML-Prediction.git /app

# Install dependencies inside Conda environment
RUN pip install --no-cache-dir -r /app/requirements.txt

# Set Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Specify the command to run on container start
CMD ["conda", "run", "-n", "myenv", "python", "Prediction_main.py"]
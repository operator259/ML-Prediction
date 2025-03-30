# Use the official Miniconda image as a base image
FROM continuumio/miniconda3:latest

# Set the working directory inside the container
WORKDIR /app

# Install build-essential for compiling
RUN apt-get update \
    && apt-get install -y build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create a Conda environment with minimal packages
RUN conda create --name myenv python=3.8

# Activate the Conda environment
RUN echo "conda activate myenv" >> ~/.bashrc


# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install any dependencies specified in requirements.txt
RUN /bin/bash -c "source ~/.bashrc && pip install --no-cache-dir -r requirements.txt"

# Set the environment variable for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Specify the command to run on container start
CMD ["/bin/bash", "-c", "source ~/.bashrc && python Prediction_main.py"]
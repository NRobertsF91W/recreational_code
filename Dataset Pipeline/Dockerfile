# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install pymongo

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variables
ENV MONGO_HOST mymongodb
ENV MONGO_PORT 27017
ENV MONGO_USERNAME admin
ENV MONGO_PASSWORD adminpassword

# Run the command to initialize the database
CMD ["sh", "-c", "python initialize_db.py && python verify_db.py"]


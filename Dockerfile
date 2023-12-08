# Use an official Python runtime as a parent image
FROM python:3.10
RUN pip install --upgrade pip

# Set the working directory to /app
WORKDIR /app

# Copy all the contents of the current dir to /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

ENV NAME myenv

# Run the Flask application
CMD ["python", "app3.py", "--host=0.0.0.0", "--port=5000"]
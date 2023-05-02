# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /hello
WORKDIR /app

# Copy the current directory contents into the container at /hello
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
# Use ENV <variable_name> <variable_value> to define env variables
# such as database connections or API keys
ENV NAME World
ENV PYTHONPATH /app

# Run app.py when the container launches
CMD ["python", "main.py"]

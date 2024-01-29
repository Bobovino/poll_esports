# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Install system dependencies for psycopg2
RUN apt-get update \
    && apt-get install -y libpq-dev gcc \
    && apt-get clean

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /code
WORKDIR /code

# Copy the requirements.txt file into the container at /code
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' myuser

# Change the ownership of the /code directory
RUN chown -R myuser:myuser /code
USER myuser

# Copy the entire Django project directory into the container at /code
COPY . /code/

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV PYTHONPATH=/code/poll_esports:$PYTHONPATH

# Run the command to start uWSGI
CMD ["gunicorn", "poll_esports.wsgi:application", "--bind", "0.0.0.0:8000"]

# Start from a Python 3.10 image
FROM python:3.10

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file into the image
COPY requirements.txt /app/

# Install the Python dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application into the image
COPY . /app/

# Add the entrypoint script
ADD docker-entrypoint.sh /app/

# Make the entrypoint script executable
RUN chmod +x /app/docker-entrypoint.sh

# Create a directory for the SQLite database
RUN mkdir /db

# Specify the entrypoint script to run when the container starts
ENTRYPOINT ["/app/docker-entrypoint.sh"]
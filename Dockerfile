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

# Create a directory for the SQLite database
RUN mkdir /db

# Specify the command to run when the container starts
CMD ["sh", "-c", "python manage.py makemigrations && \
                python manage.py migrate && \
                python manage.py runserver 0.0.0.0:8000"]
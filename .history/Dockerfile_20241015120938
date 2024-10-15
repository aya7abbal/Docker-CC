# Use the Alpine version of Python to reduce size
FROM python:3.9-alpine

# Set the working directory inside the container
WORKDIR /home/data

# Copy only necessary files
COPY script.py /home/data/
COPY IF.txt /home/data/
COPY AlwaysRememberUsThisWay.txt /home/data/

# Ensure output directory exists
RUN mkdir -p /home/data/output

# Run your Python script
CMD ["python", "script.py"]
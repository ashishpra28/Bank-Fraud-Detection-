# Base image 
FROM python:3.14-slim 

# Set working directory     
WORKDIR /app 

# Copy requirements and run all the dependencies 
COPY requirements.txt . 
RUN pip install -r requirements.txt 

# Copy rest of application code 
COPY . . 

# Expose the application port 
EXPOSE 8000
EXPOSE 8501

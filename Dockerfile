# Building on Python 3.14 base to start
FROM python:3.14-slim

# Set working directory
WORKDIR /app

# Set the requirements file
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the code
COPY . .

# Open port(s)
EXPOSE 5000

# Run command
CMD ["flask", "--app", "src/Pyle/app.py", "run", "--host=0.0.0.0"]
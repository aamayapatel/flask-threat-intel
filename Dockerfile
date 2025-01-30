# Step 1: Use an official Python runtime as a base image
FROM python:3.13-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the current project files into the container
COPY . .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port that Flask runs on
EXPOSE 5000

# Step 6: Command to run the application
CMD ["python", "app.py"]

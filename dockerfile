FROM python:3.10
# Set the working directory inside the container
WORKDIR /app
# Copy the requirements file to the working directory
COPY . /app
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 8000


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

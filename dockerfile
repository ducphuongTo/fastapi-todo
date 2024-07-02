FROM python:3.10
# Set the working directory inside the container
WORKDIR /app
# Copy the requirements file to the working directory
COPY requirements.txt .
# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the migration script into the container
COPY run_migrations.sh .

RUN chmod +x /app/run_migrations.sh
# Copy the application code to the working directory
COPY . .

EXPOSE 8000

ENTRYPOINT ["/app/run_migrations.sh"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

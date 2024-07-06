FROM python:3.10
# Set the working directory inside the container
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app


CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000"]

FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./ /app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]
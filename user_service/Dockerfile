FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

EXPOSE 8081

CMD ["uvicorn", "user_service_base.main:app", "--host", "0.0.0.0", "--port", "8081"]

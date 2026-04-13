FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY modelo_ecommerce.pkl .
COPY colunas_ecommerce.pkl .
COPY main.py .
COPY index.html .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
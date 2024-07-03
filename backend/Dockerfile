FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

EXPOSE 80

COPY ./app /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

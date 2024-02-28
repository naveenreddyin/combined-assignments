FROM python:3.9

WORKDIR /

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt --upgrade

COPY . .

CMD ["uvicorn", "src:app", "--host", "0.0.0.0", "--port", "9000"]

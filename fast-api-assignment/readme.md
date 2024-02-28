# FastAPI assignment API

FastAPI project based on Python 3.9.

## Installation

### With Docker

1. Build with docker:
```
docker build -t fast-api-assignment .
```
2. Run with docker:
```
docker run --rm -d -p 8080:9000 fast-api-assignment
```
You can access the api docs at `http://127.0.0.1:8080/docs`

### Without Docker:

1. Create a new virtual environment and install the `requirements.txt`:
```
pip install -r requirements.txt
```

2. Run the following command to run the app:
```
python app.py
```

You can now access the api docs at `http://127.0.0.1:8000/docs`

## Tests

If you want to run the tests, simply run the following command from the root folder:
```
pytest 
```

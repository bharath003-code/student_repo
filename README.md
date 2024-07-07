1. Use F1 on VS code and type create virtual environment for python
2. Choose .venv


Run fast api endpoints
```
uvicorn main:app --host 0.0.0.0 --port 8001
```

To test APIs use post man tool
Example Student POST data.
{"first_name": "John", "last_name": "Doe", "address": "123 Main St", "date_of_birth": "2000-01-01", "email": "john@example.com"}

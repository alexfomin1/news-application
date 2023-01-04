FROM python:3.10.9-slim
WORKDIR backend/
COPY . .
RUN pip install -e .
CMD ["uvicorn", "backend.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
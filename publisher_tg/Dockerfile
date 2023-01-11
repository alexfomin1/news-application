FROM python:3.10.9-slim

WORKDIR publisher_tg/
COPY . .
RUN pip install -e .
CMD ["python", "publisher_tg/main.py"]

FROM python:3.10.9-slim

WORKDIR publisher_tg/
COPY . .

RUN pip install -e .
RUN aerich init -t parser_rss.config.POSTGRES_CONFIG_AERICH

CMD ["python", "parser_rss/main.py"]

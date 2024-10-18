FROM python:3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY . .

RUN pipenv install

EXPOSE 8080

CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
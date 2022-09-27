FROM python:3.8.10-slim-buster
WORKDIR /app
COPY . .
ENTRYPOINT ["python3","password-generator.py"]


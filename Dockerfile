FROM python:3.9
WORKDIR /app
COPY ./src/ .
RUN pip install -r /app/requirements.txt

EXPOSE 5000
CMD ["python", "/app/api/api.py"]
FROM python:3.9
WORKDIR /app
COPY ./src/requirement* requirement.txt
RUN pip install -r requirement.txt
COPY ./src .

USER 1000:1000

EXPOSE 5000
CMD ["python","api/api.py"]
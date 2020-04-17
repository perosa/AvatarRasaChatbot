FROM python:3.7-alpine

COPY . /app/rest
WORKDIR /app
RUN pip install -r rest/requirements.txt

ENTRYPOINT ["python"]
CMD ["rest/resources.py"]




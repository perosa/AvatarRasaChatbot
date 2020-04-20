FROM python:3.7-alpine

COPY . /rest

RUN pip install -r rest/requirements.txt

ENTRYPOINT ["python"]
CMD ["rest/resources.py"]




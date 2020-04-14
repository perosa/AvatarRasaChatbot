FROM python:3.7-alpine

COPY ./rest /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["resources.py"]




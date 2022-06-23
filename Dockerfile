FROM python:3.10
RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install -r requirements-no-tensorflow.txt
CMD ["python", "app.py"]


EXPOSE 5000
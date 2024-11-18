FROM python:3.9-slim
WORKDIR /app
COPY ./testapp/main.py /app
RUN pip install flask
EXPOSE 4000
CMD ["python", "main.py"]

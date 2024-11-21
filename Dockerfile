FROM python:3.9-slim
WORKDIR /app
COPY main.py /app
RUN pip install flask
EXPOSE 4000
CMD ["python3", "main.py"]

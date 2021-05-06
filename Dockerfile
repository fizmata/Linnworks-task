FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-flask python3 gunicorn && \
    pip3 install Werkzeug boto3
WORKDIR /app
COPY main.py /app/main.py
COPY upload.html /app/templates/upload.html
CMD ["gunicorn", "--workers", "1", "--bind", "[::]:5000", "main:app", "--timeout", "90"]
#EXPOSE 5000/tcp

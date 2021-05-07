FROM ubuntu
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-flask python3 gunicorn && \
    pip3 install boto3 && \
    echo $HOME
WORKDIR /app
COPY credentials /root/.aws/credentials
COPY main.py /app/main.py
COPY upload.html.j2 /app/templates/upload.html.j2
COPY redirect.html /app/templates/redirect.html.j2

CMD ["gunicorn", "--workers", "1", "--bind", "[::]:5000", "main:app", "--timeout", "90"]
#EXPOSE 5000/tcp

from flask import Flask, render_template, request, send_file
from werkzeug import secure_filename
import boto3
app = Flask(__name__)

############### bucket name goes here ###############
bucket = 'lintask'
#####################################################

client = boto3.client('s3')

@app.route('/')
def upload_file():
    response = client.list_objects(Bucket=bucket)
    StatusCode = response['ResponseMetadata']['HTTPStatusCode']
    objects = response['Contents']
    return render_template('upload.html.j2', objects=objects, StatusCode=StatusCode)

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_files():
    if request.method == 'POST':
        f = request.files['file']
        client.put_object(Key=f.filename, Body=f.stream, Bucket=bucket)
        return 'file uploaded successfully'

@app.route('/download/<key>')
def download_file(key):
    client.download_file(Bucket=bucket, Key=key, Filename=key)
    return send_file('./'+key, as_attachment=True)

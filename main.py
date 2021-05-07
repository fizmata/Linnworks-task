from flask import Flask, render_template, request, Response
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
        file = request.files['file']
        client.put_object(Key=file.filename, Body=file.stream, Bucket=bucket)
        return render_template('redirect.html.j2')

@app.route('/download/<key>')
def download_file(key):
    file = client.get_object(Key=key ,Bucket=bucket)
    return Response(
        file['Body'].read(),
        mimetype=file['ContentType'],
        headers={"Content-Disposition": "attachment", "filename": key})

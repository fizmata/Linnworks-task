### Setup
To run the project you'll need:
- docker/ docker-compose
- access credentials for S3 bucket

credentials_template need to be filled with AWS credentials and renamed credentials, I'm not uploading my private info for obvious reasons.

bucket name needs to be changed in `main.py`

To build and run interactively:

  `docker-compose up --build`

To run in background:

  `docker-compose up --build -d`
  
  ---
### Description
**Technologies used**
- Docker
- Flask
- Gunicorn
- pip
- boto3
- jinja2

Docker container is used to run the application, `Dockerfile` uses Ubuntu image because there is no gunicorn on apline, with single apt-get command installs `pip3`, `gunicorn`, `flask` and `python3`, `pip3` is used to isntall `boto3` - python librery used for interfacing with S3 storage. `/app` is set to be working directory, `main.py` is copied to working directory, jinja tamplates are copied to `/app/templates/` for flask to render and amazon IAM credentials are copied to `~/.aws/credentials`. Finally gunicron creates worker for flask app and binds it to `localhos:5000`.

Docker-compose builds docker file with network mode host (maping container ports to host ports one to one) and restart policy `on-failure`.

Flask renders the pages, handles file upload to srerver and download to user.

Gunicorn is an http server

From boto library I'm using:
- list_objects to create object listing
- put_object to upload the file
- get_object

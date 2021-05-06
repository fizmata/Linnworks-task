To run the project you'll need:
- docker/ docker-compose
- access credentials for S3 bucket

credentials_template need to be filled with AWS credentials and renamed credentials, I'm not uploading my private info for obvious reasons.

bucket name needs to be changed in `main.py`

To build and run interactively:

  `docker-compose up --build`

To run in background:

  `docker-compose up --build -d`

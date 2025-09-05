import boto3
from flask import Flask, request
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
S3_BUCKET = os.getenv("S3_BUCKET")  # from secret


@app.route("/")
def home():
    return "Hello from AWS RDS + S3 via Flask!"


@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400

    # Upload to S3
    s3 = boto3.client("s3")
    s3.upload_fileobj(file, S3_BUCKET, file.filename)

    return f"File '{file.filename}' uploaded successfully to {S3_BUCKET}!", 200


if __name__ == "__main__":
    # Start Flask server
    app.run(host="0.0.0.0", port=5000)


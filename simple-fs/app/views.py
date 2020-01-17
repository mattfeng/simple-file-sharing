#!/usr/bin/env python

import boto3
import uuid
import pugsql
import random
import os

from flask import Blueprint, render_template, send_file, request
from werkzeug.utils import secure_filename

main_page = Blueprint('main', __name__, template_folder = 'templates')

def get_s3():
    sess = boto3.Session(
        aws_access_key_id = os.environ['ACCESS_KEY_ID'],
        aws_secret_access_key = os.environ['SECRET_ACCESS_KEY']
        )
    s3 = sess.client('s3')

    return s3

def generate_stub():
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    return ''.join([random.choice(alphabet) for _ in range(5)])

@main_page.route('/')
def main():
    return render_template('main.html')


@main_page.route('/u', methods = ['POST'])
def upload():
    if 'file' not in request.files:
        return 'no file'

    upload_file = request.files['file']

    if upload_file.filename == '':
        return 'no selected file'

    key = secure_filename(upload_file.filename)
    stub = generate_stub()
    
    queries = pugsql.module(os.environ['QUERIES_PATH'])
    queries.connect(os.environ['DB_CONNECTION_URL'])

    s3 = get_s3()
    s3.upload_fileobj(upload_file, os.environ['S3_BUCKET'], key)
    queries.insert_stub(stub = stub, key = key)

    return stub

@main_page.route('/d/<stub>')
def download(stub):
    queries = pugsql.module(os.environ['QUERIES_PATH'])
    queries.connect(os.environ['DB_CONNECTION_URL'])

    s3 = get_s3()
    bucket = os.environ['S3_BUCKET']

    result = queries.key_from_stub(stub = stub)
    if result is None:
        return 'invalid'
    key = result['key']

    tmp_file = '/tmp/{}'.format(uuid.uuid4())

    with open(tmp_file, 'wb') as data:
        s3.download_fileobj(bucket, key, data)

    return send_file(tmp_file, attachment_filename = key)


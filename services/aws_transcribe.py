import os
import time
from boto3.session import Session
from .utils import load_env, random_string


load_env()
ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION = os.getenv('AWS_REGION')
session = Session(aws_access_key_id=ACCESS_KEY_ID,
                  aws_secret_access_key=SECRET_ACCESS_KEY,
                  region_name=REGION)


def upload_s3(file_path, remote_path, bucket_name):
    client = session.resource('s3')
    client.Bucket(bucket_name).upload_file(file_path, remote_path)
    base_url = 'https://s3-ap-northeast-1.amazonaws.com/{}/{}'
    url = base_url.format(bucket_name, remote_path)
    return url


def transcribe(file_uri,
               wait_time=500/1000, # 500ms
               timeout=10, # times
               job_name=None):
    if not job_name:
        job_name = random_string(10)
    client = session.client('transcribe')
    client.start_transcription_job(
        TranscriptionJobName=job_name,
        Media={'MediaFileUri': file_uri},
        MediaFormat='wav',
        MediaSampleRateHertz=44100,
        LanguageCode='ja-JP',
        Settings={
            'VocabularyName' : 'aws',
            'ShowSpeakerLabels' : True,
            'MaxSpeakerLabels' : 3
        }
    )
    count = 0
    while True:
        count += 1
        if count > timeout:
            raise Exception('operation timeout')
        time.sleep(wait_time)
        status = client.get_transcription_job(TranscriptionJobName=job_name)
        if status.get('TranscriptionJobStatus') == 'COMPLETED':
            media = status.get('Transcript', {}).get('TranscriptFileUri')
            return media

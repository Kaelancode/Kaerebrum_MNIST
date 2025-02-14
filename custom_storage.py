from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings


class MediaStorage(S3Boto3Storage):
    #bucket_name = 'digits-objects'
    location =  settings.MEDIAFILES_LOCATION


class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION

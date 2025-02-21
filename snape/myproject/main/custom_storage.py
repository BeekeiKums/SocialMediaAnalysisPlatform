from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.contrib.staticfiles.utils import get_files
from django.contrib.staticfiles.storage import StaticFilesStorage
import os

class MediaStorage(FileSystemStorage):
    """Custom storage class for media files that ensures directories exist"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
        
    def save(self, name, content, max_length=None):
        # Ensure the directory exists before saving
        directory = os.path.dirname(os.path.join(settings.MEDIA_ROOT, name))
        os.makedirs(directory, exist_ok=True)
        return super().save(name, content, max_length)

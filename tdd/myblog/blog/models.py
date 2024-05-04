from django.db import models
import os

# Create your models here.
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    
    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return f'[{self.pk}] {self.title}'
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
    
    # 파일명 가져오기
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)
    
    # 확장자 가져오기
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
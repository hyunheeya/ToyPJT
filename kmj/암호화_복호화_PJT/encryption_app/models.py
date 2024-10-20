from django.db import models
from my_pjt import settings

class Encryption(models.Model):
    content = models.CharField(max_length=255)
    key = models.CharField(max_length=4)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='encryptions')  # 사용자 정보 저장

class Decryption(models.Model):
    content = models.CharField(max_length=255)
    key = models.CharField(max_length=4)
    

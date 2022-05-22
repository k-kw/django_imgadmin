from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Upimage(models.Model):
    # on_deleteが必須 DO_NOTHINGは主レコードが削除されても何もしない
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    img = models.ImageField(upload_to='upimg/', blank=True)
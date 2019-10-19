import uuid
import os

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    def get_file_path(instance, filename):
        ext = filename.split('.')[-1]
        filename = "%s.%s" % (uuid.uuid4(), ext)
        return os.path.join('img', filename)

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.title
        
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to=get_file_path)
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)





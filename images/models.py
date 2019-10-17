from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Poster(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(null=True)
    image = models.ImageField(upload_to='img')
    private = models.BooleanField(default=False)
    author = models.ForeignKey(Poster, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.pub_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)



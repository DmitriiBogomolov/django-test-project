from django.db import models
from django.conf import settings


# Create your models here.
class Message(models.Model):
    class Meta():
        db_table = "message"

    email = models.EmailField(max_length=35)
    message = models.TextField(max_length=255)
    date = models.DateTimeField()
    sent = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_DEFAULT,
                             default=-1)

    def __str__(self):
        return self.message

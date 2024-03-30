from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    from_who = models.ForeignKey(User, on_delete=models.PROTECT, default=None, related_name='from_user')
    to_who = models.ForeignKey(
        User, on_delete=models.PROTECT, default=None, related_name="to_user"
    )
    message = models.TextField()
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    has_been_seen = models.BooleanField(null=True, default=False)


# Create your models here.

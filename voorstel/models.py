from django.db import models
from random import choice


# Create your models here.

STATUS_CHOICES = (
    ("NEW", "Nieuw"),
    ("ACCEPTED", "Geaccepteerd"),
    ("DENIED", "Afgewezen"),
)
CHARSET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

class AmendementComment(models.Model):
    amendement = models.ForeignKey('Amendement')
    time = models.DateTimeField(auto_now=True)
    author = models.CharField(max_length=64)
    text = models.TextField()

    def __unicode__(self):
        return (u"%s: %s" % (self.author, self.text))[:128]


class Amendement(models.Model):
    key = models.SlugField()
    title = models.CharField(max_length=256)
    status = models.CharField(max_length=16, choices=STATUS_CHOICES)
    email = models.EmailField()

    def __unicode__(self):
        return self.title

    def gen_random_key(self):
        self.key = "".join([choice(CHARSET) for i in range(32)])



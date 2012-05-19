from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ("NEW", "Nieuw"),
    ("ACCEPTED", "Geaccepteerd"),
    ("DENIED", "Afgewezen"),
)


class AmendementComment(models.Model):
    amendement = models.ForeignKey(AMendement)
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





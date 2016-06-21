from django.db import models


GENDER_CHOICES = (
    (1, 'Male'),
    (2, 'Female')
    )


class UserProfile(models.Model):
    mobile_no = models.CharField(max_length=12)
    gender = models.IntegerField(default=None, choices=GENDER_CHOICES)


class HomeBanner(models.Model):
    """
    Home Banner Images can be strored here..!
    """
    name = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(max_length=200, blank=True, null=True)
    images = models.ImageField(upload_to='static/images')
    active = models.BooleanField(default=False)
    order = models.IntegerField(unique=True)

    def __unicode__(self):
        return "%s" % (self.name)

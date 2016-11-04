from django.db import models
from django.conf import settings

# Create your models here.
class Farm(models.Model):
    name = models.CharField(max_length=50)
    # owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

class UserProfile(models.Model):
    user_auth_id = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='userprofile')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    # pub_date = models.DateTimeField('date published')


class FarmWorker(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    #Will be good to add some other infomation.
class CrewLeaderCertificate(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    certificate_name = models.CharField(max_length=100)
    experation_date = models.DateTimeField('date expired')

class Roaster(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    date = models.DateField()
    type = models.CharField(max_length=50)

class RosterRecord(models.Model):
    farm_worker = models.ForeignKey(FarmWorker)
    roaster = models.ForeignKey(Roaster)
    status = models.BooleanField()

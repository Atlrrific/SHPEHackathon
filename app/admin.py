from django.contrib import admin
from django.apps import apps
from django.contrib.admin.sites import AlreadyRegistered

# Register your models here.
from .models import Farm, FarmWorker, CrewLeaderCertificate, Roaster, RosterRecord
# admin.site.register(FarmWorker)
# admin.site.register(CrewLeaderCertificate, Roaster)
# admin.site.register( RosterRecord)


app_models = apps.get_app_config('app').get_models()
try:
    admin.site.register(Farm)
    # admin.site.register(Friend, FriendAdmin)
except AlreadyRegistered:
    pass

for model in app_models:
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

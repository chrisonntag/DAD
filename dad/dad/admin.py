from django.contrib import admin
from django.apps import apps
from items.models import Exhibition, Item, MediaType, Comment, Like, Favorite


for model in apps.get_models():
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass


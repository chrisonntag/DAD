from django.contrib import admin
from random_app.models import Post
from items.models import Exhibition, Item, MediaType, Comment, Like, Favorite


admin.site.register(Exhibition)
admin.site.register(Item)
admin.site.register(MediaType)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Favorite)


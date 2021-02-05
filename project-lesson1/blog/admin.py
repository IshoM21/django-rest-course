from django.contrib import admin
from .models import Post
from .models import TeamSoccer
from .models import Player

# Register your models here.

admin.site.register(Post)
admin.site.register(TeamSoccer)
admin.site.register(Player)
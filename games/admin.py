from django.contrib import admin

# Register your models here.
from games.models import Game

class GameAdmin(admin.ModelAdmin):
    fields = ['name', 'platform', 'server','pub_date']
    list_display = ('name', 'platform', 'server')

admin.site.register(Game, GameAdmin)

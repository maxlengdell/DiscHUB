from django.contrib import admin
from .models import Disc
# Register your models here.

class DiscAdmin(admin.ModelAdmin):
    list_display = ('title','description','speed')


admin.site.register(Disc,DiscAdmin)
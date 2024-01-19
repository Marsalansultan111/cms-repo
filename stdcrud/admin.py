from django.contrib import admin
from .models import stdModel

class stdAdmin(admin.ModelAdmin):
    list_display=('firstname','lastname')


admin.site.register(stdModel,stdAdmin)

# Register your models here.

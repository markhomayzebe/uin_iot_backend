from django.contrib import admin

# Register your models here.
from detektor_suhu.models import Stats

admin.site.register(Stats)


def _str_(self):
    return f'Temp = {self.temperature} dan humidity = {self.humidity}'


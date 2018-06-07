from django.contrib import admin

# Register your models here.

from .models import usuario
from .models import partida
from .models import equipos


admin.site.register(usuario)
admin.site.register(partida)
admin.site.register(equipos)

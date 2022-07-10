from django.contrib import admin

# Register your models here.
from .models import Linguagem
admin.site.register(Linguagem)

from .models import Empresa
admin.site.register(Empresa)

from .models import Programador
admin.site.register(Programador)
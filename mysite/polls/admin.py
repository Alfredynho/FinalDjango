from django.contrib import admin

# Register your models here.
#Registrando los modelos
from .models import Question , Choice
admin.site.register(Question)
admin.site.register(Choice)

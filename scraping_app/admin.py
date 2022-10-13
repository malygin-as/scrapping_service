from django.contrib import admin
from .models import City, CodeLang, Vacancy, Error

# Register your models here.
admin.site.register(City)
admin.site.register(CodeLang)
admin.site.register(Vacancy)
admin.site.register(Error)

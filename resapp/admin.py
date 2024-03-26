from django.contrib import admin

from .models import ModelCv, CreateContact,Portfolio,Education,Skills,Experience

# Register your models here.
admin.site.register(ModelCv),
admin.site.register(CreateContact),
admin.site.register(Portfolio),
admin.site.register(Education),
admin.site.register(Skills),
admin.site.register(Experience),



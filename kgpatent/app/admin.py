from django.contrib import admin
from .models import *

admin.site.register(Applicant)
admin.site.register(Patent)
admin.site.register(Code)
admin.site.register(Mark)
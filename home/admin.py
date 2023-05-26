from django.contrib import admin
from .models import HomeEnquiry,booking,HomeHomechoose
# Register your models here.
admin.site.register(booking)
admin.site.register(HomeHomechoose)
admin.site.register(HomeEnquiry)
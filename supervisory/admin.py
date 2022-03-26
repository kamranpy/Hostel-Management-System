from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Customer)
admin.site.register(Hostel)
admin.site.register(Rooms)
admin.site.register(HostelApply)
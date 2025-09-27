from django.contrib import admin
from .models import Registration

class RegistrationAdmin(admin.ModelAdmin):
    list_display =(
        'name','email','phone','message','gender','country'
    )
admin.site.register(Registration,RegistrationAdmin)    

# Register your models here.

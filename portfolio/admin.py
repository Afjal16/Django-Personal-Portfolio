from django.contrib import admin
from portfolio.models import Contact,Blog

# Register your models here.
class contactAdmin(admin.ModelAdmin):
    list_display=('name', 'email', 'number', 'description')
    
class blogAdmin(admin.ModelAdmin):
    list_display=('title', 'authname', 'description', 'img', 'timestamp')
    search_fields=('title', 'authname')
    
admin.site.register(Contact,contactAdmin)
admin.site.register(Blog,blogAdmin)
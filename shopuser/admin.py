from django.contrib import admin
from .models import Shopuser

# Register your models here.
class ShopuserAdmin(admin.ModelAdmin):
    list_display = ('email', )

admin.site.register(Shopuser, ShopuserAdmin)


from django.contrib import admin
from .models import Product,Offer
# Register your models here.


class Productadmin(admin.ModelAdmin):
    list_display=('name','price','stock')
    
class Offeradmin(admin.ModelAdmin):
    list_display=('code','discount')


admin.site.register(Product,Productadmin)
admin.site.register(Offer,Offeradmin)
from django.contrib import admin

from product.models import Product,Suits,Pants, WomenSuit,Accessories,UserHasSuits,Sales,DataDash

# Register your models here.
admin.site.register(Product)
admin.site.register(Suits)

admin.site.register(Pants)

admin.site.register(WomenSuit)

admin.site.register(Accessories)

admin.site.register(UserHasSuits)

admin.site.register(Sales)

admin.site.register(DataDash)

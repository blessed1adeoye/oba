from django.contrib import admin
from .models import Category, HomeCarousel, Product, JumiaProduct, JumiaCarousel


admin.site.register(HomeCarousel)
admin.site.register(JumiaProduct)
admin.site.register(Product)
admin.site.register(JumiaCarousel)
from django.contrib import admin

from applications.product.models import Product, ProductImage


class InLineProductImage(admin.TabularInline):
    model = ProductImage
    extra = 1
    fields = ['image', ]


class ProductAdminDisplay(admin.ModelAdmin):
    inlines = [InLineProductImage, ]
    # fields = ['title', 'price']


admin.site.register(Product, ProductAdminDisplay)

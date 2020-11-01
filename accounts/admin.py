from django.contrib import admin
from .models import User
from order.models import Order
from location.models import Location
from menu.models import MenuItem
from posts.models import Post

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    pass
class OrderAdmin(admin.ModelAdmin):
    pass
class LocationAdmin(admin.ModelAdmin):
    pass
class MenuItemAdmin(admin.ModelAdmin):
    pass
class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UserAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Post, PostAdmin)

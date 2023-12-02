from django.contrib import admin

from main_app.models import User, Resource

# Register your models here.
admin.site.site_header = "Dev's resources"
admin.site.index_title = "Dev's"


class UserAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "user_type"]


class ResourceAdmin(admin.ModelAdmin):
    pass


class ResourceAdmin(admin.ModelAdmin):
    list_display = ["name", "link", "desc"]


admin.site.register(User, UserAdmin)
admin.site.register(Resource, ResourceAdmin)

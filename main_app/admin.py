from django.contrib import admin

from main_app.models import User

# Register your models here.
admin.site.site_header = "Dev's resources"
admin.site.index_title = "Dev's"


class UserAdmin(admin.ModelAdmin):
    pass


class UserAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "user_type"]


admin.site.register(User, UserAdmin)

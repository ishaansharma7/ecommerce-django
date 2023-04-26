from django.contrib import admin
from accounts.models import AllUsers


@admin.register(AllUsers)
class AdminNewUser(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'is_staff')
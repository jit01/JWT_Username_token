from django.contrib import admin

from jwt_username_app.models import emp


class empAdmin(admin.ModelAdmin):
    list_display = ['name', 'sal']


admin.site.register(emp, empAdmin)


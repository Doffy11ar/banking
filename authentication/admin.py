from django.contrib import admin
from .models import Country, Departments, Cities, Users
# Register your models here.
admin.site.register(Country)
admin.site.register(Departments)
admin.site.register(Cities)
admin.site.register(Users)


class CountryAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev', 'get_status')

    def get_status(self, obj):
        return "Active" if obj.status else "Inactive"
        get_status.short_description = 'Status'
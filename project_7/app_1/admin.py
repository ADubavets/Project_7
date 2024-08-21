from django.contrib import admin
from .models import ComputerisationTechnical


class ComputerisationTechnicalAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'parse_datetime', 'description']
    list_display_link = ['id', 'price']
    search_fields = ['id', 'price', 'parse_datetime', 'description']
    list_filter = ['price', 'parse_datetime']


admin.site.register(ComputerisationTechnical, ComputerisationTechnicalAdmin)

from django.contrib import admin
from .models import Candidate

class CandidateAdmin(admin.ModelAdmin):
    # Display fields in list view
    list_display = ('name', 'email', 'age', 'gender', 'phone_number')
    
    # Add search functionality
    search_fields = ('name', 'email', 'phone_number')
    
    # Add filters
    list_filter = ('gender', 'age')
    
    # Fieldsets for better organization
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email', 'phone_number')
        }),
        ('Additional Information', {
            'fields': ('age', 'gender'),
            'classes': ('collapse',)
        }),
    )
    
    # Make name and email clickable in admin list
    list_display_links = ('name', 'email')
    
    # Set default ordering
    ordering = ('name',)
    
    # Uncomment if you add created_at field later:
    # date_hierarchy = 'created_at'

# Register the model with admin
admin.site.register(Candidate, CandidateAdmin)
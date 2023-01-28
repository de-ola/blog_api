from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)

class ContactInLineTable(admin.TabularInline):
    model = ContactDetails
    fields = [
        'name',
        'url',
    ]

class QuestionAdmin(admin.ModelAdmin):
    fields = '_all_'
    list_display = '_all_'
    inlines = [
        ContactInLineTable,
    ]

admin.site.register(User, QuestionAdmin)
admin.site.register(ContactDetails)
from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):

    list_display = ('post', 'owner', 'report_reason', 'created_on')

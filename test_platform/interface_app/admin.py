from django.contrib import admin
from .models import TestCase


class TestCaseAdmin(admin.ModelAdmin):
    list_display = ['module', 'name', 'url', 'req_method',
                    'req_type', 'req_header', 'req_parameter', 'responses_assert']


admin.site.register(TestCase, TestCaseAdmin)



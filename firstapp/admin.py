from django.contrib import admin
from .import models
from .models import Branch
from .models import Notice
from .models import Profile
from django.contrib.admin.options import ModelAdmin

# Register your models here.


class NoticeAdmin(ModelAdmin):
    list_display = ["subject", "cr_date"]
    search_fields = ["subject", "msg"]
    list_filter = ["cr_date"]


admin.site.register(models.Notice, NoticeAdmin)

admin.site.register(Branch)
admin.site.register(Profile)


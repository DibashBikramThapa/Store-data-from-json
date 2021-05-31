from django.contrib import admin
from .import models

# Register your models here.

class ReportAdmin(admin.ModelAdmin):

     field=['id','year','petroleum_product','sale','country']

     search_fields=['year','petroleum_product','country']

     list_filter=['year','petroleum_product','country']

     list_display=['year','petroleum_product','country','sale']

admin.site.register(models.Report,ReportAdmin)

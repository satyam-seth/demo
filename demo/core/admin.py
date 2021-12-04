from django.contrib import admin
from .models import Org,Emp

# Register your models here.

@admin.register(Org)
class OrgAdmin(admin.ModelAdmin):
    list_display=['id','name','registered_on','last_modified']

@admin.register(Emp)
class OrgAdmin(admin.ModelAdmin):
    list_display=['id','name','org','registered_on','last_modified']
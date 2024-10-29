from django.contrib import admin
from app.models import *
class WebPageAdminView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=('name',)
    list_per_page=3
    list_display_links=['url']
    search_fields=['name','url']
    list_filter=['url','name','topic_name']
# Register your models here.
admin.site.register(Topic)
admin.site.register(WebPage,WebPageAdminView)
admin.site.register(AccessRecord)
admin.site.site_header='Python Developer'
admin.site.site_title='Developer'
admin.site.index_title='Developed By Aditya'
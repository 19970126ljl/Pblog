from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import MUSER,MARTICLE,MCOMMENT,MPHOTO,MALBUM,MPUBLISH
# Register your models here.

class MUSERInline(admin.TabularInline):
    model = MUSER
    can_delete = False
    verbose_name = 'MUSER'
    verbose_name_plural = 'MUSERs'

class UserAdmin(BaseUserAdmin):
    inlines = (MUSERInline,)

class MARTICLEAdmin(admin.ModelAdmin):
    list_display=['id','title','writer','content','ctime','audit']
    list_editable=['title','writer','content','audit']
    list_per_page = 10

class MCOMMENTAdmin(admin.ModelAdmin):
    list_display=['id','user','article','content','ctime']
    list_editable=['content']
    list_per_page = 10
    
class MALBUMAdmin(admin.ModelAdmin):
    list_display=['id','user','title','cover','ctime']
    list_editable=['user','title','cover']
    list_per_page = 10

class MPHOTOAdmin(admin.ModelAdmin):
    list_display=['id','title','album','pic','ctime']
    list_editable=['title','album','pic']
    list_per_page = 10

class MPUBLISHAdmin(admin.ModelAdmin):
    list_display=['id','article','photo','comment','ctime']
    list_editable=['article','photo','comment']
    list_per_page = 10

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(MARTICLE,MARTICLEAdmin)
admin.site.register(MCOMMENT,MCOMMENTAdmin)
admin.site.register(MPHOTO,MPHOTOAdmin)
admin.site.register(MALBUM,MALBUMAdmin)
admin.site.register(MPUBLISH,MPUBLISHAdmin)

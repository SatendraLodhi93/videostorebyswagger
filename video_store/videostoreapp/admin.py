from django.contrib import admin
from .models import video_model
# Register your models here.
class video_model_admin(admin.ModelAdmin):
    list_display=['id','name','video']
admin.site.register(video_model,video_model_admin)
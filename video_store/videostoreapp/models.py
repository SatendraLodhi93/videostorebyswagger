from django.db import models

# Create your models here.
class video_model(models.Model):
    def nameFile(instance, filename):
         return '/'.join(['videos', str(instance.name), filename])
    name = models.CharField(max_length=100)
    video=models.FileField(upload_to=nameFile,blank=True)
    
    

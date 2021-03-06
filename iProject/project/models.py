from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    project_by=models.CharField(max_length=14)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    #content=models.TextField()
    content= RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + " by " + self.project_by


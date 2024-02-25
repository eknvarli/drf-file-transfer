from django.db import models


# Create your models here.
class File(models.Model):
    title = models.CharField(max_length=100)
    content = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'file'
        verbose_name = 'File'
        verbose_name_plural = 'Files'

    def __str__(self):
        return self.title
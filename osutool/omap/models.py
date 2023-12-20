from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class oMap(models.Model):
    category = models.ForeignKey(Category, related_name='omaps', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    star_rating = models.FloatField()
    length = models.FloatField()
    image = models.ImageField(upload_to='omap_images', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Maps'

    def __str__(self):
        return self.name
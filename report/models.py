from django.db import models

# Create your models here.
class Report(models.Model):

    year=models.IntegerField(max_length=4)
    petroleum_product=models.CharField(max_length=264)
    sale=models.IntegerField(primary_key=True)
    country=models.CharField(max_length=264)

    def __str__(self):
        return self.country

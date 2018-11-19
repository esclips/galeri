from django.db import models


class Kategori(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name

# Create your models here.
class GaleriItem(models.Model):

    name = models.CharField(max_length=150)
    image = models.ImageField()
    category = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category.name + ' / ' + self.name



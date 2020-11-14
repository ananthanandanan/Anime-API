from django.db import models

# Create your models here.

class ProductModel(models.Model):
    """Model definition for ProductModel."""

    # TODO: Define fields here
    Segment = models.CharField(max_length = 100)
    Country = models.CharField(max_length = 100)
    Product = models.CharField(max_length = 100)
    Units = models.IntegerField()
    Sales = models.IntegerField()
    Datesold = models.CharField(max_length = 100)
    

    class Meta:
        """Meta definition for ProductModel."""

        verbose_name = 'ProductModel'
        verbose_name_plural = 'ProductModels'

    def __str__(self):
        """Unicode representation of ProductModel."""
        
        return self.Product

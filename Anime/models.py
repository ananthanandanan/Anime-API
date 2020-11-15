from django.db import models

# Create your models here.

    
class AnimeModel(models.Model):
    """Model definition for AnimeModel."""

    # TODO: Define fields here
    Anime_id = models.IntegerField()
    Name = models.CharField(max_length=200)
    Genre = models.CharField(max_length=300)
    Type = models.CharField(max_length=200)
    Episode = models.IntegerField()
    Rating = models.FloatField()
    Members = models.IntegerField()

    class Meta:
        """Meta definition for AnimeModel."""

        verbose_name = 'AnimeModel'
        verbose_name_plural = 'AnimeModels'

    def __str__(self):
        """Unicode representation of AnimeModel."""
        
        return self.Name

    
    

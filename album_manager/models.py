from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Album(models.Model):
    title = models.CharField(max_length=45, null=False)
    year_release = models.PositiveIntegerField(null=False)
    gender = models.CharField(max_length=45)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.title} - {self.artist}'
